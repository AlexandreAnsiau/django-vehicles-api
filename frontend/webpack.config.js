const miniCssExtractPlugin = require('mini-css-extract-plugin')
const path = require('path');

module.exports = {
  mode: 'production',
  entry: {
    "bootstrap": "./src/js/bootstrap.js",
    "custom": "./src/js/custom.js",
  },
  output: {
    filename: "[name].js",
    path: path.resolve(__dirname, "../static/dist/js"),
  },
  plugins: [new miniCssExtractPlugin({filename: "../css/[name].css"})],
  module: {
    rules: [
        {
            test: /\.(scss)$/,
            use: [miniCssExtractPlugin.loader, "css-loader", "sass-loader"]
        }
    ]
  }
};