Reflux = require 'reflux'

BirdActions = require './actions'


BirdTypesStore = Reflux.createStore
  listenables: BirdActions

  getInitialState: ->
    count: 0
    items: []

  onLoadTypes: ->
    console.log 'load types started'

  onLoadTypesCompleted: (body) ->
    console.log 'load types complete'
    @updateTypes(body)

  updateTypes: (body) ->
    console.log 'updated types store'
    @trigger
      count: body.count
      items: body.results


module.exports = BirdTypesStore
