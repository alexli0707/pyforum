var webpack = require('webpack');
var distDir = './dist';

module.exports = {
    entry: {
        // cats:'./src/cats.js',
        'vendor': ['jquery', 'bootstrap'],
        'init_common': './src/init_common.js',
        'custom/app': './src/app.js',
    },
    output: {
        path: distDir,
        filename: '[name].js'
    },
    // watch: true,
    //压缩代码
    plugins: [
        // new webpack.optimize.UglifyJsPlugin({
        //     compress: {
        //         warnings: false,
        //     },
        //     output: {
        //         comments: false,
        //     },
        // }),
        //配置Jquery全局名称
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery"
        }),
        //公共引用的js单独打包
        new webpack.optimize.CommonsChunkPlugin(/* chunkName= */'vendor', /* filename= */'vendor.js')
    ],


    module: {
        preLoaders: [
            {
                test: /\.js$/, // include .js files
                exclude: /node_modules/, // exclude any and all files in the node_modules folder
                loader: "jshint-loader"
            }
        ],
        loaders: [
            {test: /bootstrap\/js\//, loader: 'imports?jQuery=jquery'},
            {test: /\.css$/, loader: "style-loader!css-loader"},
            { test: /\.(eot|woff|woff2|svg|ttf)([\?]?.*)$/, loader: "file-loader" },
        ]
    },
    // more options in the optional jshint object
    jshint: {
        // any jshint option http://www.jshint.com/docs/options/
        // i. e.
        camelcase: true,

        // jshint errors are displayed by default as warnings
        // set emitErrors to true to display them as errors
        emitErrors: false,

        // jshint to not interrupt the compilation
        // if you want any file with jshint errors to fail
        // set failOnHint to true
        failOnHint: false,

        // custom reporter function
        reporter: function (errors) {
        }
    }
};