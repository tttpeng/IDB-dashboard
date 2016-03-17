
var path = require('path');
var nodeModulesPath = path.resolve(__dirname, 'node_modules');

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
    module: {
        loaders: [
            {test: /\.js$/, exclude: /node_modules/, loader: "babel-loader", query: {presets: ['react', 'es2015']}}
        ]

    },
    resolveLoader: {
        root: path.join(__dirname, 'node_modules')
    }
}