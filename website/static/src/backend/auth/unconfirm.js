/**
 * Created by walker on 16/12/1.
 */
define(function (require, exports, module) {
    var $ = requirejs('jquery');
    var toastr = requirejs('toastr');
    var Util = require('src/backend/util');
    $(function () {
        $('#btnSend').click(function(event){
            $.ajax({
                url: Util.formatUrl('auth/confirm'),
                type: 'GET',
            }).done(function (parm) {
                toastr.success('发送成功');
            });
        })
    });
});