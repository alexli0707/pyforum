/**
 * Created by walker on 16/12/4.
 */
define(function (require, exports, module) {
    var $ = require('jquery');
    var toastr = require('toastr');
    var Util = require('util');

    var helper = {
        getData: function () {
            var email = $.trim($('#email').val());
            var username = $.trim($('#username').val());
            var password = $.trim($('#password').val());
            var password_confirm = $.trim($('#password_confirm').val());

            return {
                'email': email,
                'username': username,
                'password': password,
                'password_confirm': password_confirm,
            }
        },
        validData: function (data) {
            var item = data['email'];
            if (Util.isEmpty(item)) {
                toastr.warning('请填写Email')
                return false;
            }
            var item = data['username'];
            if (Util.isEmpty(item)) {
                toastr.warning('请填写昵称')
                return false;
            }
            var password = data['password'];
            if (Util.isEmpty(password)) {
                toastr.warning('请填写密码')
                return false;
            }
            var password_confirm = data['password_confirm'];
            if (Util.isEmpty(password_confirm)) {
                toastr.warning('请填写确认密码')
                return false;
            }
            if(password!=password_confirm){
                toastr.warning('两次填写的密码不一样')
                return false;
            }

            return true;
        }
    };

    $(function () {
        $('#register').click(function (event) {
            console.log('inini');
            var data = helper.getData();
            if (helper.validData(data)) {
                $.ajax({
                    url: Util.formatUrl('auth/register'),
                    type: 'POST',
                    data: Util.stringify(data)
                }).done(function (parm) {
                    toastr.success(parm)
                    Util.redirect('');
                });
            }
        })
    });
});