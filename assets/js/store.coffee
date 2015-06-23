Reflux = require 'reflux'
request = require 'superagent'

BirdActions = require './actions'


BirdStore = Reflux.createStore
  linstenables: [BirdActions]

  init: ->
    @listenTo(BirdActions.load, @fetchData)

  getInitialState: ->
    @birds = []

  fetchData: ->
    request.get '/api/birds/?only_leafs=true', (err, res) =>
      @updateBirds(res.body)

  updateBirds: (birds) ->
    @birds = birds
    @trigger(birds)


module.exports = BirdStore
