React = require('react/addons')
ReactCSSTransitionGroup = React.addons.CSSTransitionGroup
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
Button = require 'react-bootstrap/lib/Button'
ButtonGroup = require 'react-bootstrap/lib/ButtonGroup'
Portal = require 'react-bootstrap/lib/Portal'

MainContainer = require './MainContainer'

VirtualList = require './virtual-list/VirtualList'


BirdRow = React.createClass
  propTypes:
    height: React.PropTypes.number

  getInitialState: ->
    highlightedPerm: {}

  handleHighlightPerm: (perm) ->
    {highlightedPerm} = @state
    setPerm = if highlightedPerm.id is perm.id then {} else perm
    @setState
      highlightedPerm: setPerm

  renderPermutationsHeader: (bird) ->
    {highlightedPerm} = @state
    type_groups = _.map bird.permutations, (perm) =>
      <Button
          key={perm.id}
          onClick={@handleHighlightPerm.bind(@, perm)}
          active={perm.id is highlightedPerm.id}
          bsSize="xsmall">
        {_.pluck(perm.types, 'name').join(', ')}
      </Button>
    <ButtonGroup className="permutations">
      {type_groups}
    </ButtonGroup>

  renderThumbnailGroup: (images, perm, size=5) ->
    showDate = false
    showPerm = true

    images.map (image) ->
      thumbnail = _.find(image.sizes, size: size)
      formated_date = new Date(image.date_added).toLocaleString()
      <Col xs={12} sm={4} md={3} key={image.vibe_uuid}>
        <Thumbnail src={thumbnail and thumbnail.url}>
          {image.credit}
          {if showDate then (
            <small>
              <time date={image.date_added}>{formated_date}</time>
            </small>
          )}
        </Thumbnail>
      </Col>

  render: () ->
    {bird, height} = @props

    thumbnails = permThumbnails = []

    # Get non permutation based images
    if (images = bird.details.representative_images) and images.length > 0
      thumbnails = @renderThumbnailGroup(images)

    # Get
    if bird.permutations.length > 0
      permThumbnails = _.map bird.permutations, (perm) =>
        @renderThumbnailGroup(perm.details.representative_images)

    permHeader = @renderPermutationsHeader(bird)

    <ListGroupItem
        style={height: height, overflow: 'hidden'}
        key={bird.id}>
      <Row>
        <Col md={6}>
          <h4 title={bird.id}>{bird.name} </h4>
        </Col>
        {if bird.permutations.length then (
          <Col md={6} className="permutations-header">
            <h5>permutations:</h5>
            {permHeader}
          </Col>
        ) else (
          <Col md={6}>
            <h5>no permutations</h5>
          </Col>
        )}
        <Col md={12}>
          <Row>
            {thumbnails.concat(permThumbnails)}
          </Row>
        </Col>
      </Row>
    </ListGroupItem>


BirdsList = React.createClass
  mixins: [
    Reflux.connect(BirdStore, 'birds')
  ]

  getInitialState: ->
    birdBoxHeight: 300

  componentDidMount: ->
    BirdActions.load()

  renderBird: (bird) ->
    <BirdRow
      height={@state.birdBoxHeight}
      bird={bird}/>

  render: ->
    {birds, birdBoxHeight} = @state

    if birds.loading
      loadingBackdrop = (
        <div key={Math.floor(Math.random()*100)} className="loading-backdrop">
          <span className="loading-indicator">
            <div className="pacman">
              <div></div>
              <div></div>
              <div></div>
              <div></div>
              <div></div>
            </div>
          </span>
        </div>
      )

    <MainContainer>
      <ReactCSSTransitionGroup transitionName="loading-backdrop">
        {loadingBackdrop}
      </ReactCSSTransitionGroup>
      <VirtualList
        scrollDelay={10}
        className="list-group"
        items={birds.items}
        renderItem={@renderBird}
        itemHeight={birdBoxHeight}/>
    </MainContainer>


module.exports = BirdsList
