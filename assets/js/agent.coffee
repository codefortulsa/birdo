Promise = this.Promise || require('promise')
module.exports = require('superagent-promise')(require('superagent'), Promise)
