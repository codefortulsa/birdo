React = require('react')
Reflux = require 'reflux'
_ = require 'lodash'

BirdActions = require './actions'
BirdStore = require './store'

Col = require 'react-bootstrap/lib/Col'
Row = require 'react-bootstrap/lib/Row'
Thumbnail = require 'react-bootstrap/lib/Thumbnail'
ListGroup = require 'react-bootstrap/lib/ListGroup'
ListGroupItem = require 'react-bootstrap/lib/ListGroupItem'
Thumbnail = require 'react-bootstrap/lib/Thumbnail'

MainContainer = require './MainContainer.cjsx'

VirtualList = require 'react-virtual-list/dist/VirtualList'


BirdsList = React.createClass
  mixins: [Reflux.connect(BirdStore, 'birds')]

  getInitialState: ->
    birdBoxHeight: 300

  componentDidMount: ->
    BirdActions.load()

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
        <Col md={3}>
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
    <MainContainer style={paddingTop: 60}>
      <div>{amount} birds yo</div>
      <ListGroup>
        <VirtualList items={birds} renderItem={@renderBird} itemHeight={(birdBoxHeight) + 10}/>
      </ListGroup>
    </MainContainer>


module.exports = BirdsList
