/**
 * Created by walker on 17/1/15.
 */
define(function (require, exports, module) {
    var $ = requirejs('jquery');
    var toastr = requirejs('toastr');
    var Util = require('src/backend/util');
    var helper = {
        getData: function () {
            var title = Util.trimValById('title');
            var summary = Util.trimValById('summary');
            var content = this.getEditorData();
            return {
                'title': title,
                'summary': summary,
                'content': content,
            };
        },
        validData: function (data) {
            var item = data['title'];
            if (Util.isEmpty(item)) {
                toastr.warning('请填写标题');
                return false;
            }
            var item = data['summary'];
            if (Util.isEmpty(item)) {
                toastr.warning('请填写文章概要');
                return false;
            }
            var item = data['content'];
            if (Util.isEmpty(item)) {
                toastr.warning('请填写内容');
                return false;
            }
            return true;
        },
        getEditorData:function () {
            return ckEditor.getData();
        }


    };
    module.exports = helper;
});