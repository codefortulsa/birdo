/**
 * Webpack development configuration
 */
/*globals __dirname:false */

var path = require("path");
var webpack = require("webpack");
var base = require("./webpack.config");
// var CleanPlugin = require("clean-webpack-plugin");
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var BundleTracker = require('webpack-bundle-tracker');

var output_path = base.output.path;

module.exports = {
  cache: true,
  context: base.context,
  entry: base.entry,
  output: {
    path: output_path,
    filename: "bundle.js",
    publicPath: "http://127.0.0.1:2992/js/"
  },
  module: base.module,
  resolve: base.resolve,
  resolveLoader: base.resolveLoader,
  devtool: "eval-source-map",
  stylus: base.stylus,
  plugins: [
    // new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),
    new BundleTracker({path: __dirname, filename: 'webpack-stats.json'}),
    // if an asset errors during compiling don't include it.
    // new webpack.NoErrorsPlugin()
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify(process.env.NODE_ENV)
      }
    }),
    new ExtractTextPlugin('[name].css', {allChunks: true}),
    new webpack.ResolverPlugin.ResultSymlinkPlugin()
  ]
};
