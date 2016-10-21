/**
 * Created by walker on 16/10/20.
 */
//加载bootstrap css资源
require('bootstrap/dist/css/bootstrap.css');
require('toastr/build/toastr.css');
require('toastr/toastr.js');
var helper = {
    getCsrfToken: function () {
        if (csrfToken) {
            _csrfToken = csrfToken;
            csrfToken = null;
        }
        return _csrfToken;
    },
}

$(function () {
    var toastr = require('toastr');
    var doc = $(document);
    doc.ajaxSend(function (e, xhr, settings) { // 开始一个ajax请求
        // tip.show({
        //     text: '正在载入数据...',
        //     timer: 2000,
        //     hideTimer: 30000
        // });
        toastr.options = {
            "closeButton": false,
            "debug": false,
            "newestOnTop": false,
            "progressBar": true,
            "positionClass": "toast-top-right",
            "preventDuplicates": false,
            "onclick": null,
            "showDuration": "300",
            "hideDuration": "1000",
            "timeOut": "2000",
            "extendedTimeOut": "30000",
            "showEasing": "swing",
            "hideEasing": "linear",
            "showMethod": "fadeIn",
            "hideMethod": "fadeOut"
        }
        toastr.info('正在载入数据...');
    }).ajaxStart(function () { // 开始一个ajax请求且无其他ajax请求过程

    }).ajaxSuccess(function (e, xhr, settings) { // 一个ajax成功
        // helper.highlight(helper.getPath(settings.url));
        toastr.clear();
    }).ajaxError(function (e, xhr, settings, err) { // 一个ajax失败
        if (err !== 'abort') {
            var msg = xhr && xhr.responseJSON && xhr.responseJSON.meta && xhr.responseJSON.meta.message;
            toastr.error(msg || err || '服务器异常');
        } else {
            toastr.clear();
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


    // if ($.support.pjax) {
    //     doc.on('click', 'a[data-pjax]',function (e) {
    //         $.pjax.click(e, {
    //             container: $(this).attr('data-pjax') || '#main'
    //         });
    //     }).on('submit', 'form[data-pjax]',function (e) {
    //         $.pjax.submit(e, $(this).attr('data-pjax'));
    //     }).on('pjax:success', function () {
    //         helper.loadScript();
    //     });
    // }
    // // 应对页面刷新
    // helper.loadScript();
});

