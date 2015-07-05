Reflux = require 'reflux'
request = require 'superagent'

BirdActions = require './actions'


BirdStore = Reflux.createStore
  listenables: BirdActions

  birds: []
  prevResult: {}

  getInitialState: ->
    count: 0
    items: @birds
    offset: 0
    loading: false

  onLoad: ->
    console.log 'load birds started'
    # set the loading sate to true
    @trigger
      count: @prevResult.count || 0
      items: @birds
      offset: 0
      loading: true

  onLoadCompleted: (body) ->
    console.log 'load birds completed'
    @prevResult = body
    # detect if offset is > 0 and then append birds
    @updateBirds(body)

  onLoadFailed: (reason) ->
    # Does this get called on failure?

  # Need to add to existing bird list unless searching, in which case it's reset
  updateBirds: (body, append=false) ->
    console.log 'updating birds store'
    @birds = if not append then body.results else @birds = @birds.concat(body.results)
    @trigger
      count: body.count
      items: @birds
      offset: 0
      loading: false


module.exports = BirdStore
