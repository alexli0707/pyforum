define(function (require, exports, module) {
    var $ = require('jquery');

    var Util = {
            getBaseUrl: function () {
                return window['baseurl'];
            },
            formatUrl: function (url) {
                return Util.getBaseUrl() + url;
            },
            stringify: function (data) {
                return JSON.stringify(data);
            },
            redirect: function (url, container) {
                window.location.href = Util.formatUrl(url);
            },
            getUNIXTimestamp: function () {
                return (new Date().getTime()) / 1000;
            },
            isEmpty: function (item) {
                return !(item && item.trim());
            },
            isEmptyArray: function (item) {
                if (typeof image_array !== 'undefined' && image_array.length > 0) {
                    return false;
                } else {
                    return true;
                }
            },
            trimValById:function (targetId) {
               return $.trim($('#'+targetId).val());
            },
            getUrlParameter: function (sParam) {
                var sPageURL = decodeURIComponent(window.location.search.substring(1)),
                    sURLVariables = sPageURL.split('&'),
                    sParameterName,
                    i;

                for (i = 0; i < sURLVariables.length; i++) {
                    sParameterName = sURLVariables[i].split('=');

                    if (sParameterName[0] === sParam) {
                        return sParameterName[1] === undefined ? true : sParameterName[1];
                    }
                }
            },
            redirectNextUrl: function (defaultUrl) {
                var nextUrl = this.getUrlParameter('next');
                if (nextUrl){
                    window.location.href =nextUrl;
                }else{
                    window.location.href = defaultUrl;
                }
            },
            isNotEmpty: function (item) {
                return item && item.trim();
            }
            ,
            isUrl: function (url) {
                return /^(http|https):\/\/[a-zA-Z0-9._-]+(\.[a-zA-Z0-9._-]+){1,}(\/\S*)*$/.test(url);
            }
            ,
            hasLeadingOrTailingSpace: function (str) {
                return /^\s+|\s+$/.test(str);
            }
            ,
            editor: function (params) {
                params = params || {};
                require.async(['editor', Util.getBaseUrl() + 'admin/themes/thirdpart/css/ueditor.css'], function (Editor) {
                    params.tipNode && $(params.tipNode).remove();

                    var content = $('#myEditor').data('content');
                    if (!content) {
                        content = '';
                    }

                    var ue = Editor.getEditor('myEditor', {
                        toolbars: [
                            [
                                'FullScreen', 'Bold', 'Italic', 'InsertOrderedList', 'InsertUnorderedList', 'Paragraph',
                                '|', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyJustify',
                                '|', 'photo', 'video', 'links',
                                '|', 'Source', 'RemoveFormat',
                                '|', 'inserttable', 'deletetable', 'insertrow', 'deleterow'
                            ]
                        ],
                        wordCount: true,
                        elementPathEnabled: false,
                        initialFrameHeight: 300,
                        initialFrameWidth: 800,
                        initialContent: params.content ? params.content : content,
                        contextMenu: [],
                        topOffset: 56
                    });
                    Page.reg(params.ins || 'myEditor', ue);
                    params.callback && params.callback(ue, Editor);
                });
            }
            ,
            //提取外部图片到服务器
            uploadUrlImage: function (opt) {
                var self = this;
                opt = $.extend(true, {
                    url: '',
                    uri: '',
                    onSuccess: function () {
                    },
                    onFail: function () {
                    },
                    onComplete: function () {
                    }
                }, opt);
                if (!opt.url) {
                    return self;
                }
                var targetUri = (opt.uri) ? opt.uri : 'urlimages?url='
                console.log('targetUri:' + targetUri);
                console.log('url:' + self.formatUrl(targetUri + encodeURIComponent(opt.url)))
                $.ajax({
                    async: false,
                    url: self.formatUrl(targetUri + encodeURIComponent(opt.url)),
                    type: 'PUT'
                }).done(function (data) {
                    opt.onSuccess(data);
                }).complete(function () {
                    opt.onComplete();
                });
                return self;
            }
            ,
            //上传单张图片
            createUpload: function (name, uri, maxSize) {
                name = name || 'icon';  //对应模板里上传图片input的id (<input type="file" id="icon"/>)
                uri = uri || 'images';  //图片上传处理地址
                maxSize = maxSize || '3MB'; //文件大小限制
                return Upload({
                    url: Util.formatUrl(uri),
                    node: '#' + name,
                    type: '*.jpg; *.gif; *.png',
                    maxSize: maxSize, // 文件大小限制
                    maxCount: -1, // 文件数量限制，-1不限制
                    multi: false, // 是否允许多文件上传
                    max: 1,
                    fileName: 'file',
                    data: {},
                    ins: 'upload_game_icon'
                }).on('successAdd', function (file, files) { // 成功加入队列
                    this.get('node').attr('disabled', 'disabled');
                }).on('success', function (file, data) { // 上传成功
                    if (data) {
                        data = data.data;
                        $('#' + name + '_preview').html('<img src="' + data.url + '" data-src="' + data.src + '" width="72"/>');
                    }
                }).on('complete', function (file) { // 上传文件完成，无论失败成功
                    this.get('node').removeAttr('disabled');
                });
            }
            ,
            createSingleIconUpload: function (name, uri, maxSize) {
                uri = uri || 'images';  //图片上传处理地址
                maxSize = maxSize || '300KB'; //文件大小限制
                Util.createUpload(name, uri, maxSize)
            }
            ,
            //关联查询
            lunch_query: function (query_url, need_id_show) {
                $('#keyword').each(function () {
                    var that = $(this);
                    new AutoComplete({
                        trigger: that,
                        filter: function (data) {
                            return data;
                        },
                        itemTemplate: function (data) {
                            if (need_id_show) {
                                return '<li data-role="item" data-value="' + data.id + '">' + data.id + ':' + data.name + '</li>';
                            }
                            return '<li data-role="item" data-value="' + data.id + '">' + data.name + '</li>';
                        },
                        dataSource: function (value) {
                            var that = this;
                            $.ajax({
                                url: Util.formatUrl(query_url),
                                data: {key: value},
                                dataType: 'json',
                                success: function (data) {
                                    that.trigger('data', data.data);
                                },
                                error: function (data) {
                                    that.trigger('data', []);
                                }
                            });
                        }
                    }).render().on('itemSelect', function (data) {
                        var trigger = this.get('trigger');
                        trigger.val('');

                        //var extra_data = JSON.stringify([data.id]);
                        var extra_data = data.id;
                        $('#data').val(data.name).attr('data-extra_data', extra_data);
                        $('#forum_icon').attr('src', data.icon);

                        setTimeout(function () {
                            trigger.blur();
                        }, 100);
                    });
                });
            }
            ,

            //排序
            changeOrder: function (e, node, uri) {
                if (e.type === 'keyup' && e.keyCode === 13) {
                    var that = $(node);
                    var tr = $(node).closest('tr');
                    var id = tr.attr('data-id');
                    var ord = parseInt(that.val()) || 0;

                    $.ajax({
                        url: Util.formatUrl(uri + '/' + id),
                        type: 'POST',
                        data: JSON.stringify({ord: ord}),
                        dataType: 'json',
                        success: function (data) {
                            location.reload();
                        },
                        error: function (data) {
                        }
                    });
                }
            }
            ,

            //推荐
            recommend: function (e, node, uri) {
                var id = node.val();
                var status = node.prop('checked') ? 1 : 0;
                $.ajax({
                    url: Util.formatUrl(uri + '/' + id),
                    type: 'POST',
                    data: Util.stringify({'status': status})
                }).done(function (parm) {
                    tip.success('操作成功');
                });
            }
            ,

            //日期插件
            createCalender: function (id, only_day) {
                var time_format = true;

                if (only_day) {
                    time_format = {
                        hour: false,
                        minute: false
                    }
                }

                new Calendar({
                    trigger: id || '#ptime',
                    zIndex: 9999,
                    time: time_format
                });
            }
            ,

            //排序查询
            sort_by_column: function (obj) {
                if (obj.hasClass('sorttable-nosort')) {
                    return;
                }
                var order;
                if (obj.hasClass('sorttable-sorted-reverse')) {
                    order = 'asc';
                } else if (obj.hasClass('sorttable-sorted')) {
                    order = 'desc';
                } else {
                    var defaultorder = obj.data('defaultorder');
                    order = defaultorder ? defaultorder : 'desc';
                }
                var classes = obj.attr('class');
                var column_reg = /sorttable-column-(\d+)/;
                var column_name = classes.match(column_reg);
                $('#sorttable_column').val(column_name[1]);
                $('#sorttable_order').val(order);
                $('#msearch').submit();
            }
            ,


        }
        ;
    module.exports = Util;
});
