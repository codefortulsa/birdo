React = require("react")

utils =
  areArraysEqual: (a, b) ->
    return false  if not a or not b
    return false  unless a.length is b.length
    i = 0
    length = a.length

    while i < length
      return false  unless a[i] is b[i]
      i++
    true

  topDifference: (element, container) ->
    @topFromWindow(element) - @topFromWindow(container)

  topFromWindow: (element) ->
    return 0  if not element or element is window
    element.offsetTop + @topFromWindow(element.offsetParent)

scrollticker = null
lastScrollTop = null

VirtualList = React.createClass(
  propTypes:
    items: React.PropTypes.array.isRequired
    itemHeight: React.PropTypes.number.isRequired
    renderItem: React.PropTypes.func.isRequired
    container: React.PropTypes.object.isRequired
    tagName: React.PropTypes.string.isRequired
    scrollDelay: React.PropTypes.number

  getDefaultProps: ->
    container: (if typeof window isnt "undefined" then window else `undefined`)
    tagName: "div"
    scrollDelay: null

  getVirtualState: (props) ->

    # default values
    state =
      items: []
      bufferStart: 0
      height: 0

    # early return if nothing to render
    if typeof props.container is "undefined" or props.items.length is 0 or props.itemHeight <= 0 or not @isMounted()
      return state

    items = props.items

    # total heigh
    state.height = props.items.length * props.itemHeight
    container = props.container

    viewHeight = (if typeof container.innerHeight isnt "undefined" then container.innerHeight else container.clientHeight)

    # no space to render
    if viewHeight <= 0
      return state

    list = @getDOMNode()

    offsetTop = utils.topDifference(list, container)

    viewTop = (if typeof container.scrollY isnt "undefined" then container.scrollY else container.scrollTop)

    renderStats = VirtualList.getItems(viewTop, viewHeight, offsetTop, props.itemHeight, items.length)

    # no items to render
    if renderStats.itemsInView is 0
      return state
    state.items = items.slice(renderStats.firstItemIndex, renderStats.lastItemIndex + 1)
    state.bufferStart = renderStats.firstItemIndex * props.itemHeight
    console.log(state)
    state

  getInitialState: ->
    @getVirtualState @props

  shouldComponentUpdate: (nextProps, nextState) ->
    return true  if @state.bufferStart isnt nextState.bufferStart

    # if (this.state.bufferEnd !== nextState.bufferEnd) return true;
    return true  if @state.height isnt nextState.height
    equal = utils.areArraysEqual(@state.items, nextState.items)
    not equal

  componentWillReceiveProps: (nextProps) ->
    state = @getVirtualState(nextProps)
    @props.container.removeEventListener "scroll", @onScroll
    nextProps.container.addEventListener "scroll", @onScroll
    @setState state

  componentDidMount: ->
    state = @getVirtualState(@props)
    @setState state
    @props.container.addEventListener "scroll", @onScroll

  componentWillUnmount: ->
    @props.container.removeEventListener "scroll", @onScroll

  onScroll: ->
    if !@props.scrollDelay
      @updateVirtualState()
    else
      if !scrollticker
        that = this
        scrollticker = window.setInterval((->
          container = that.props.container
          scrollTop = if typeof container.scrollY != 'undefined' then container.scrollY else container.scrollTop
          if lastScrollTop == scrollTop
            window.clearInterval scrollticker
            scrollticker = null
            that.updateVirtualState()
          else
            lastScrollTop = scrollTop
          return
        ), @props.scrollDelay)

  updateVirtualState: ->
    state = @getVirtualState(@props)
    @setState state

  render: ->
    <ul {...@props} style={{boxSizing: 'border-box', height: @state.height, paddingTop: @state.bufferStart }} >
        {@state.items.map(this.props.renderItem)}
    </ul>
)

VirtualList.getBox = (view, list) ->
  list.height = list.height or list.bottom - list.top
  top: Math.max(0, Math.min(view.top - list.top))
  bottom: Math.max(0, Math.min(list.height, view.bottom - list.top))

VirtualList.getItems = (viewTop, viewHeight, listTop, itemHeight, itemCount) ->
  return itemsInView: 0  if itemCount is 0 or itemHeight is 0
  listHeight = itemHeight * itemCount
  listBox =
    top: listTop
    height: listHeight
    bottom: listTop + listHeight

  viewBox =
    top: viewTop
    bottom: viewTop + viewHeight


  # list is below viewport
  return itemsInView: 0  if viewBox.bottom < listBox.top

  # list is above viewport
  return itemsInView: 0  if viewBox.top > listBox.bottom

  listViewBox = VirtualList.getBox(viewBox, listBox)
  firstItemIndex = Math.max(0, Math.floor(listViewBox.top / itemHeight))
  lastItemIndex = Math.ceil(listViewBox.bottom / itemHeight)
  itemsInView = lastItemIndex - firstItemIndex + 2

  result =
    firstItemIndex: firstItemIndex
    lastItemIndex: lastItemIndex
    itemsInView: itemsInView

  result

module.exports = VirtualList
