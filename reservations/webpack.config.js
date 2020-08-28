const HTMLWebpackPlugin = require('html-webpack-plugin');

const HTMLWebpackPluginConfig = new HTMLWebpackPlugin({
    template: __dirname + '/src/index.html',
    filename: 'index.html',
    inject: 'body'
});

module.exports = {
    entry: __dirname + '/src/index.js',
    mode: 'development',
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                enforce: 'pre',
                use: ['babel-loader', 'source-map-loader']
            }, 
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
            }
        ]
    },
    output: {
        filename: 'index.js',
        path: __dirname + '/build'
    },
    plugins: [HTMLWebpackPluginConfig],
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    }
};