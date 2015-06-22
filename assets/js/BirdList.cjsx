React = require('react')
Reflux = require 'reflux'
_ = require 'lodash'

BirdActions = require './actions'
BirdStore = require './store'

Col = require 'react-bootstrap/lib/Col'
Row = require 'react-bootstrap/lib/Row'
Thumbnail = require 'react-bootstrap/lib/Thumbnail'

MainContainer = require './MainContainer.cjsx'


BirdsList = React.createClass
  mixins: [Reflux.connect(BirdStore, 'birds')]

  componentDidMount: ->
    BirdActions.load()

  renderBird: (bird) ->
    if not bird.details
      return undefined
    images = bird.details.representative_images
    thumbnail = undefined
    if images.length > 0
      thumbnail = _.find(images[0].sizes, size: 5)
    <Col xs={6} md={4}>
      <Thumbnail src={thumbnail and thumbnail.url}>
        <h5>{bird.name}</h5>
      </Thumbnail>
    </Col>

  render: ->
    {birds} = @state
    amount = 0
    console.log('renda')
    if birds
      amount = birds.length
    <MainContainer style={paddingTop: 60}>
      <div>{amount} birds yo</div>
      <Row>
        {birds.map(@renderBird)}
      </Row>
    </MainContainer>


module.exports = BirdsList
