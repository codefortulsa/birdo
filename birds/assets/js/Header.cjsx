React = require('react/addons')
Reflux = require 'reflux'

_ = require 'lodash'

Navbar = require('react-bootstrap/lib/Navbar')
Nav = require('react-bootstrap/lib/Nav')
NavItemLink = require('react-router-bootstrap/lib/NavItemLink')
Input = require('react-bootstrap/lib/Input')
DropdownButton = require('react-bootstrap/lib/DropdownButton')
Button = require('react-bootstrap/lib/Button')

require('react-select/dist/default.css')
Select = require('react-select/lib/Select')

BirdTypesStore = require './typeStore'
BirdStore = require './store'
BirdActions = require './actions'


Header = React.createClass
  mixins: [
    Reflux.connect(BirdTypesStore, 'types')
    Reflux.connect(BirdStore, 'birds')
    React.addons.LinkedStateMixin
  ]

  init: ->
    @timeout = undefined

  getInitialState: ->
    birdType: undefined
    birdName: undefined

  componentDidMount: ->
    BirdActions.loadTypes()

  selectType: (typeId) ->
    @setState
      seletedType: @state.types.items[typeId]

  checkName: ->
    {nameSearch} = @state

  typeOptions: ->
    types = _.map @state.types.items, (type) =>
      value: type.id
      label: type.name
    # types.unshift({value: undefined, label: 'All Types'})
    # shim for es6 Array.filter, due to issue in select lib not building
    types.filter = (filter_cb, ctx) ->
      _.filter(@, filter_cb.bind(ctx))
    return types

  componentWillUpdate: (nextProps, nextState)->
    if @timeout
      clearTimeout @timeout

    {birdName, birdType} = @state
    if birdName isnt nextState.birdName or birdType isnt nextState.birdType
      @timeout = setTimeout( =>
        BirdActions.load(nextState)
      , 200)
    return true

  handleClear: ->
    @setState @getInitialState()

  render: ->

    {birds} = @state

    if birds
      amount = birds.count

    typeLink = @linkState('birdType')
    handleTypeChange = (value) ->
      typeLink.requestChange(value)

    clearButton = <Button bsStyle="danger" onClick={@handleClear}>clear</Button>
    <Navbar brand="Birdo" inverse fixedTop toggleNavKey={0}>
      <Nav eventKey={0}>
        <div className="navbar-form navbar-left">
          <div className="name-group form-group">
            <Input
              type="text"
              valueLink={@linkState('birdName')}
              className="form-control"
              placeholder="Bird name"
              buttonAfter={clearButton}/>
          </div>
          <div className="type-group form-group">
            <Select
              value={typeLink.value}
              onChange={handleTypeChange}
              ignoreCase={true}
              placeholder="Filter by optional bird type…"
              noResultsText="No bird types found"
              options={@typeOptions()}/>
          </div>
        </div>
        { if amount > 0 then (
          <p className="navbar-text">found {amount} {if amount == 1 then "bird" else "birds"}</p>
        ) else (
          <p className="navbar-text">no birds found</p>
        )}
        <NavItemLink eventKey={0} to="bird-list">Birds Overview</NavItemLink>
      </Nav>
    </Navbar>


module.exports = Header
