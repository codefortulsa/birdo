Reflux = require 'reflux'
request = require 'superagent'


BirdActions = Reflux.createActions
  load:
    children: ['completed', 'failed']
  # addBird: undefined


# BirdActions.addBird.preEmit = (bird) ->
#   request.post('/api/birds')


module.exports = BirdActions
