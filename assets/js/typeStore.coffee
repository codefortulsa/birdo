Reflux = require 'reflux'

BirdActions = require './actions'


BirdTypesStore = Reflux.createStore
  linstenables: [BirdActions]

  init: ->
    @listenTo(BirdActions.loadTypes.completed, @onLoadTypesCompleted)

  getInitialState: ->
    []

  onLoadTypes: ->
    console.log 'load types started'

  onLoadTypesCompleted: (res) ->
    console.log 'load types complete'
    @updateTypes(res.body)

  updateTypes: (types) ->
    console.log 'updated types store'
    @types = types
    @trigger(types)


module.exports = BirdTypesStore
