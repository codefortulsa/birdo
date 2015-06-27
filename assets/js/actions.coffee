Reflux = require 'reflux'

request = require './agent'


BirdActions = Reflux.createActions
  load:
    asyncResult: true
  loadTypes:
    asyncResult: true


BirdActions.load.listenAndPromise (search={}) ->
  request
    .get('/api/birds/')
    .query(
      object_ype: 'leafs'
      name: search.birdName
      parent: search.birdType
    )
    .end()

BirdActions.loadTypes.listenAndPromise ->
  request
    .get('/api/birds/')
    .query(
      object_type: 'branches'
    )
    .end()


module.exports = BirdActions
