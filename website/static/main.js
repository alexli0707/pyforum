/**
 * Created by walker on 16/11/25.
 * 配置公共常用库
 */
requirejs.config({
    paths:{
        'jquery':'node_modules/jquery/dist/jquery.min',
        'toastr':'node_modules/toastr/build/toastr.min',
        'util':'src/backend/util'
    }
});

define(function (require, exports, module) {
    var $ = require('jquery');
    var toastr = require('toastr');
    var helper = {
        getPath: function (url) {
            var host = location.protocol + '//' + location.host;
            url = url.replace(host, '');
            var temp = url.split(/\?/);
            return temp ? temp[0] : url;
        },
        highlight: function (path) {
            var nav = $('.top-nav').eq(0);
            var node = nav.find('a[href="' + path + '"]').eq(0);
            var p = node.closest('.item');
            if(p[0]) {
                node = p;
            }
            if (node[0]) {
                if (!node.hasClass('curr')) {
                    nav.find('.curr').removeClass('curr');
                    node.addClass('curr');
                }
            }
        },
        getCsrfToken: function() {
            if(csrfToken) {
                _csrfToken = csrfToken;
                csrfToken = null;
            }
            return _csrfToken;
        }
    };

    $(function () {
        var doc = $(document);
       toastr.options = {
          "closeButton": false,
          "debug": false,
          "newestOnTop": false,
          "progressBar": false,
          "positionClass": "toast-top-right",
          "preventDuplicates": true,
          "onclick": null,
          "showDuration": "300",
          "hideDuration": "1000",
          "timeOut": "5000",
          "extendedTimeOut": "1000",
          "showEasing": "swing",
          "hideEasing": "linear",
          "showMethod": "fadeIn",
          "hideMethod": "fadeOut"
        }
        doc.ajaxSend(function (e, xhr, settings) { // 开始一个ajax请求
            toastr['info']('正在载入数据...')
        }).ajaxStart(function () { // 开始一个ajax请求且无其他ajax请求过程

        }).ajaxSuccess(function (e, xhr, settings) { // 一个ajax成功
            helper.highlight(helper.getPath(settings.url));
            toastr.clear();
        }).ajaxError(function (e, xhr, settings, err) { // 一个ajax失败
            if (err !== 'abort') {
                var msg = xhr && xhr.responseJSON && xhr.responseJSON.meta && xhr.responseJSON.meta.message;
                toastr.clear();
                var errorMsg = msg || err || '服务器异常';
                console.log(errorMsg)
                toastr.error(errorMsg);
            } else {
                toastr.clear();
                toastr.error('服务器异常');
            }
        }).ajaxComplete(function (e, xhr, settings) { // 一个ajax完成

        }).ajaxStop(function () { // 所有ajax完成

        });

        // AJAX全局设置
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                // 设定csrf_token
                xhr.setRequestHeader('csrf-token', helper.getCsrfToken());
            },
            contentType: 'application/json',
            dataType: 'json'
        });
    });

});