#应用后台前端框架说明.

目前后台采用Webpack + pjax 实现单页式运用

编码方式使用CommonJs规范,init_common.js为js初始化脚本,dist/vendor.js为jquery + bootstrap+pjax通用资源抽取打包,这样可以保证所有引用这些模块的js文件在压缩打包后体积较小.
由于后端同学前端水平有限,后台的前端项目尽量用最简方式实现,避免太多的框架以及过度封装.
