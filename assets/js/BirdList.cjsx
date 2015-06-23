React = require('react/addons')
Reflux = require 'reflux'
_ = require 'lodash'

BirdActions = require './actions'
BirdStore = require './store'

Col = require 'react-bootstrap/lib/Col'
Row = require 'react-bootstrap/lib/Row'
Thumbnail = require 'react-bootstrap/lib/Thumbnail'
ListGroup = require 'react-bootstrap/lib/ListGroup'
Input = require 'react-bootstrap/lib/Input'
ListGroupItem = require 'react-bootstrap/lib/ListGroupItem'
Thumbnail = require 'react-bootstrap/lib/Thumbnail'

MainContainer = require './MainContainer.cjsx'

VirtualList = require 'react-virtual-list/dist/VirtualList'


BirdsList = React.createClass
  mixins: [
    Reflux.connect(BirdStore, 'birds')
    React.addons.LinkedStateMixin
  ]

  getInitialState: ->
    birdBoxHeight: 300
    nameSearch: ''

  componentDidMount: ->
    BirdActions.load()

  checkName: ->
    {nameSearch} = @state

  renderBird: (bird) ->
    {birdBoxHeight} = @state

    if not bird.details
      return undefined
    images = bird.details.representative_images
    show_date = false

    if images.length > 0
      thumbnails = images.map (image) ->
        thumbnail = _.find(image.sizes, size: 5)
        formated_date = new Date(image.date_added).toLocaleString()
        <Col xs={12} sm={4} md={3}>
          <Thumbnail src={thumbnail and thumbnail.url}>
            {image.credit}
            {if show_date then (
              <small>
                <time date={image.date_added}>{formated_date}</time>
              </small>
            )}
          </Thumbnail>
        </Col>

    <ListGroupItem style={maxHeight: birdBoxHeight, height: birdBoxHeight, overflow: 'hidden'} key={bird.id}>
      <Row>
        <Col md={12}>
          <h4>{bird.name} <small>{bird.id}</small></h4>
          <Row style={overflowX: 'scroll', whiteSpace: 'nowrap'}>
            {thumbnails}
          </Row>
        </Col>
      </Row>
    </ListGroupItem>

  render: ->
    {birds, birdBoxHeight} = @state
    amount = 0
    if birds
      amount = birds.length

    valueLink = @linkState('nameSearch')
    handleChange = (e) ->
      value = e.target.value
      valueLink.requestChange(value)
      if @timeout
        clearTimeout @timeout
      @timeout = setTimeout( =>
        BirdActions.load(value)
      , 500)

    <MainContainer style={paddingTop: 60}>
      <div>{amount} birds yo</div>
      <Input
        type="text"
        value={valueLink.value}
        onChange={handleChange}/>
      <VirtualList tagName="ul" className="list-group" items={birds} renderItem={@renderBird} itemHeight={birdBoxHeight}/>
    </MainContainer>


module.exports = BirdsList
