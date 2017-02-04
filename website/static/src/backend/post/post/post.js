/**
 * Created by walker on 17/1/15.
 */
define(function (require, exports, module) {
    var $ = requirejs('jquery');
    var toastr = requirejs('toastr');
    var Util = require('src/backend/util');
    var helper = require('./helper.js');

    var shelper = {
        addTag: function (name) {
            var tag_ele = '<span class="tag badge bg-aqua">' + name + '<i class="fa fa-fw fa-remove"></i></span>';
            $('#tagsPane').append(tag_ele);
        }
    }

    $(function () {
        $('#confirm').click(function (event) {
            var data = helper.getData();
            if (helper.validData(data)) {
                if ($(this).attr('data-action') == 'create') {
                    $.ajax({
                        url: Util.formatUrl('posts'),
                        type: 'POST',
                        data: Util.stringify(data)
                    }).done(function (parm) {
                        Util.redirectNextUrl('/posts');
                    });
                } else {
                     var post_id = $('#id').val();
                     $.ajax({
                        url: Util.formatUrl('posts/'+post_id),
                        type: 'PUT',
                        data: Util.stringify(data)
                    }).done(function (parm) {
                        Util.redirectNextUrl('/posts');
                    });
                }
            }


        });
        $('#btnSummary').click(function (event) {
            var content = helper.getEditorData();
            var dom = document.createElement("DIV");
            dom.innerHTML = content;
            var plain_text = (dom.textContent || dom.innerText);
            var summary = plain_text.substring(0, 100);
            $('#summary').val(summary);
        });
        require(['node_modules/jquery-autocomplete/jquery.autocomplete'], function (autocomplete) {
            $('#tags').autocomplete({
                source: [
                    {
                        // url: "tags/query?s=%QUERY%",
                        url: Util.formatUrl('posts/tags/query?s=%QUERY%'),
                        type: 'remote',
                        valueKey: 'title',
                        getTitle: function (item) {
                            return item['title']
                        },
                        getValue: function (item) {
                            return item['title']
                        },

                    },
                ]
            }).on('selected.xdsoft', function (e, datum) {
                shelper.addTag(datum.title);
            });
        });

        $('#tagsPane').on('click', '.badge', function () {
            $(this).remove();
        });
        $('#addTag').click(function () {
            shelper.addTag($('#tags').val())
        });
    });
});
