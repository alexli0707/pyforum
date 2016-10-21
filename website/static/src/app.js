var cats = require('./cats.js');
var toastr = require('toastr')
// var test = require('jquery');

console.log(cats);
console.log('So good');
console.log($.fn.jquery);
// toastr.info('Are you the 6 fingered man?');
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
    "timeOut": "3000",
    "extendedTimeOut": "30000",
    "showEasing": "swing",
    "hideEasing": "linear",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
}
toastr.info('正在载入数据...');
