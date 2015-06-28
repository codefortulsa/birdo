Reflux = require 'reflux'

_ = require 'lodash'

request = require './agent'


BirdActions = Reflux.createActions
  load:
    asyncResult: true
  loadTypes:
    asyncResult: true


BirdActions.load.listenAndPromise (search={}) ->
  query =
    object_ype: 'leafs'
    name: search.birdName
    parent: search.birdType

  # remove undefined/empty values
  # ( empty parent removes all leafs with parents )
  search_query = _.omit(query, (val, key) ->
    return !val
  )

  request
    .get('/api/birds/')
    .query(search_query)
    .end()

BirdActions.loadTypes.listenAndPromise ->
  request
    .get('/api/birds/')
    .query(
      object_type: 'branches'
    )
    .end()


module.exports = BirdActions
