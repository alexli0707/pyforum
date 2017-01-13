/**
 * Created by walker on 16/11/29.
 */
define(function (require, exports, module) {
    var $ = require('jquery');
    var toastr = require('toastr');
    var Util = require('src/backend/util');
    $(function () {
        $('#signIn').click(function (event) {
            var data = {
                'email': $.trim($('#email').val()),
                'password':$.trim($('#password').val()),
            }

            $.ajax({
                url: Util.formatUrl('auth/login'),
                type: 'POST',
                data: Util.stringify(data)
            }).done(function (parm) {
                Util.redirectNextUrl('/');
            });
        })
    });
});
