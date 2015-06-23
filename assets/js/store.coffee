Reflux = require 'reflux'
request = require 'superagent'

BirdActions = require './actions'


BirdStore = Reflux.createStore
  linstenables: [BirdActions]

  init: ->
    @listenTo(BirdActions.load, @fetchData)

  getInitialState: ->
    @birds = []

  fetchData: (name='') ->
    request
      .get('/api/birds/')
      .query(
        only_leafs: true
        name: name
      )
      .end (err, res) =>
        @updateBirds(res.body)

  updateBirds: (birds) ->
    @birds = birds
    @trigger(birds)


module.exports = BirdStore
