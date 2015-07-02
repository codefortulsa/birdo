/**
 * Webpack production configuration
 */
/*globals __dirname:false */

var path = require("path");
var webpack = require("webpack");
var CleanPlugin = require("clean-webpack-plugin");
var StatsWriterPlugin = require("webpack-stats-plugin").StatsWriterPlugin;
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var BundleTracker = require('webpack-bundle-tracker');
var nib = require('nib');

var output_path = path.resolve(__dirname, "../static/bundles/");

module.exports = {
  cache: true,
  context: __dirname,
  entry: "./js/app.cjsx",
  output: {
    path: output_path,
    filename: "[name].js",
    chunkFilename: "[id].js"
  },
  module: {
    loaders: [
      { test: /\.js(x|)?$/,
        include: path.join(__dirname, "client"),
        loaders: ["jsx?harmony", "babel-loader?optional[]=runtime"] },
      { test: /\.(coffee|cjsx)$/,
        loaders: ["coffee", "cjsx"]},
      { test: /\.css$/,
        loader: ExtractTextPlugin.extract("style-loader", "css-loader")},
      { test: /\.styl$/,
        loader: ExtractTextPlugin.extract("style-loader", "css-loader!stylus-loader" )},
      { test: /\.(jpe?g|png|gif|svg)$/i,
        loaders: [
            'file?hash=sha512&digest=hex&name=[hash].[ext]',
            'image-webpack?bypassOnDebug&optimizationLevel=7&interlaced=false'
        ]}
    ]
  },
  resolve: {
    extensions: ["", ".js", ".jsx", ".cjsx", ".coffee"]
  },
  stylus: {
    use: [nib()],
    import: ['variables']
  },
  plugins: [
    // ignore all moment locals
    new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),

    // Clean
    // new CleanPlugin(["bundles"]),

    // Optimize
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.UglifyJsPlugin({ output: {comments: false} }),

    // Meta, debug info.
    new webpack.DefinePlugin({
      "process.env": {
        // Signal production mode for React JS libs.
        NODE_ENV: JSON.stringify("production")
      }
    }),

    // new webpack.SourceMapDevToolPlugin(
    //   "../map/bundle.[hash].js.map",
    //   "\n//# sourceMappingURL=http://127.0.0.1:3001/dist/map/[url]"
    // ),

    new StatsWriterPlugin({
      path: output_path,
      filename: "stats.json"
    }),
    new BundleTracker({path: __dirname, filename: 'webpack-stats.json'}),
    new webpack.optimize.OccurenceOrderPlugin(true), // preferEntry true,
    new ExtractTextPlugin('[name].css', {allChunks: true})
    // new webpack.optimize.CommonsChunkPlugin("commons.chunk-[hash].js")
  ]
};
