/**
 * Created by walker on 17/1/15.
 */
define(function (require, exports, module) {
    var $ = require('jquery');
    var toastr = require('toastr');
    var Util = require('src/backend/util');
    var helper = require('./helper.js');
    $(function () {
        $('#create').click(function (event) {
            var data = helper.getData();
            if (helper.validData(data)) {
                $.ajax({
                    url: Util.formatUrl('posts'),
                    type: 'POST',
                    data: Util.stringify(data)
                }).done(function (parm) {
                    Util.redirectNextUrl('/posts');
                });
            }
        });
        $('#btnSummary').click(function (event) {
            var content = helper.getEditorData();
            var dom=document.createElement("DIV");
            dom.innerHTML=content;
            var plain_text=(dom.textContent || dom.innerText);
            var summary = plain_text.substring(0, 100);
            $('#summary').val(summary);
        });
    });
});
