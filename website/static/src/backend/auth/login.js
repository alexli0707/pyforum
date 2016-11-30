/**
 * Created by walker on 16/11/29.
 */
define(function (require, exports, module) {
    var $ = require('jquery');
    var toastr = require('toastr');
    var Util = require('util')
    $(function () {
        $('#signIn').click(function(event){
            var data = {
                'email': $.trim($('#email').val()),
                'password':$.trim($('#password').val()),
            }

            $.ajax({
                url: Util.formatUrl('auth/login'),
                type: 'POST',
                data: Util.stringify(data)
            }).done(function (parm) {
                Util.redirect('');
            });
        })
    });
});
// require(['jquery', 'toastr','backend/util'], function ($, toastr,Util) {
//     $(function () {
//         //点击登录
//          $('#signIn').click(function(event){
//             var data = {
//                 'email': $.trim($('#email').val()),
//                 'password':$.trim($('#password').val()),
//             }
//
//             $.ajax({
//                 url: Util.formatUrl('auth/login'),
//                 type: 'POST',
//                 data: Util.stringify(data)
//             }).done(function (parm) {
//                 toastr.success('修改成功');
//                 Util.redirect('propagation/carousel');
//             });
//         })
//     });
// });
