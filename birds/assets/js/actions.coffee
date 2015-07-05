Reflux = require 'reflux'

_ = require 'lodash'

request = require('superagent-bluebird-promise')


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
    offset: search.offset

  # remove undefined/empty values
  # ( as empty parent query removes all leafs with parents )
  search_query = _.omit query, (val, key) ->
    return _.isUndefined(val) or _.isEmpty(val)

  # Cancel previous request if not done
  if birdLoadRequest
    birdLoadRequest.cancel()

  birdLoadRequest = request
    .get('/api/birds/')
    .query(search_query)
    .then (res) ->
      return res.body

  return birdLoadRequest

BirdActions.loadTypes.listenAndPromise ->
  request
    .get('/api/birds/')
    .query(object_type: 'branches')
    .then (res) ->
      return res.body


module.exports = BirdActions
