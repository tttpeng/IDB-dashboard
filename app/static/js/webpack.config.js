
var path = require('path');
var nodeModulesPath = path.resolve(__dirname, 'node_modules');
var webpack = require('webpack');


module.exports = {
    entry: {
        index: "./index.js"
    },
    output: {
        path: "./build",
        filename: "bundle.js"
    },
    resolve: {
        extensions: ['', '.js', '.jsx']
    },
    plugins: [
        new webpack.ProvidePlugin({
            'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch'
        })
    ],
    module: {
        loaders: [
            {test: /\.js$/, exclude: /node_modules/, loader: "babel-loader", query: {presets: ['react', 'es2015']}}
        ]

    },
    resolveLoader: {
        root: path.join(__dirname, 'node_modules')
    }



}