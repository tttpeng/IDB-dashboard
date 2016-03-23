
var path = require('path');
var webpack = require('webpack')


module.exports = {
    entry: {
        index:  ['babel-polyfill', './index.js']
    },
    output: {
        path: "./build",
        filename: "bundle.js"
    },
    resolve: {
        root: path.join(__dirname),
        fallback: path.join(__dirname, 'node_modules'),
        modulesDirectories: ['node_modules'],
        extensions: ['', '.json', '.js', '.jsx', '.scss', '.png', '.jpg', '.jpeg', '.gif']
    },
    plugins: [
        new webpack.ProvidePlugin({
            'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch'
        })
    ],
    module: {
        loaders: [
            {test: /\.js$/, exclude: /node_modules/, loader: "babel-loader", query: {presets: ['react', 'es2015']}},
            {
            test: /\.jsx$/,
            loader: 'babel-loader!jsx-loader?harmony'
            },
            {
            test: /\.json$/,
            loader: 'json-loader'
        }

        ]

    },
    resolveLoader: {
        root: path.join(__dirname, 'node_modules')
    }



}
