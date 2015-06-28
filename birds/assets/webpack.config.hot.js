/**
 * Webpack production configuration
 */

var path = require("path");
var webpack = require('webpack');
var dev = require("./webpack.config.dev");

module.exports = {
  cache: true,
  context: dev.context,
  entry: [
    "webpack-dev-server/client",
    "webpack/hot/only-dev-server",
    dev.entry
  ],
  output: dev.output,
  module: {
    loaders: [
      { test: /\.js(x|)?$/,
        include: path.join(__dirname, "client"),
        loaders: ["react-hot", "jsx?harmony", "babel-loader?optional[]=runtime"] },
      { test: /\.(coffee|cjsx)$/,
        loaders: ["react-hot", "coffee", "cjsx"]},
      { test: /\.css$/,
        loaders: ["react-hot", "style-loader", "css-loader"]},
      { test: /\.styl$/,
        loaders: ["react-hot", "style-loader", "css-loader", "stylus-loader"]},
      { test: /\.(jpe?g|png|gif|svg)$/i,
        loaders: [
            'file?hash=sha512&digest=hex&name=[hash].[ext]',
            'image-webpack?bypassOnDebug&optimizationLevel=7&interlaced=false'
        ]}
    ]
  },
  resolve: dev.resolve,
  devtool: "eval-source-map",
  stylus: dev.stylus,
  plugins: dev.plugins.push([
    // ignore all moment locals
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin()
  ])
};
