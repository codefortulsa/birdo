Reflux = require 'reflux'
request = require 'superagent'

BirdActions = require './actions'


BirdStore = Reflux.createStore
  linstenables: [BirdActions]

  init: ->
    @listenTo(BirdActions.load.completed, @onLoadCompleted)

  getInitialState: ->
    []

  onLoad: ->
    console.log 'load birds started'

  onLoadCompleted: (res) ->
    console.log 'load birds completed'
    @updateBirds(res.body)

  updateBirds: (birds) ->
    console.log 'updating birds store'
    @trigger(birds)


module.exports = BirdStore
