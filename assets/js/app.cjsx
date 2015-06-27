React = require 'react'

Header = require './Header.cjsx'
BirdList = require './BirdList.cjsx'
MainContainer = require './MainContainer.cjsx'

RouteHandler = require 'react-router/lib/components/RouteHandler'

require '../css/styles.styl'


AppBase = React.createClass
  render: ->
    <div>
      <Header/>
      <RouteHandler/>
    </div>


NotFound = React.createClass
  render: ->
    <div>
      <Header/>
      <MainContainer>
        <h2>Nothing found for that url!</h2>
      </MainContainer>
    </div>


Route = require 'react-router/lib/Route'
runRouter = require 'react-router/lib/runRouter'
DefaultRoute = require 'react-router/lib/components/DefaultRoute'
NotFoundRoute = require 'react-router/lib/components/NotFoundRoute'


routes = (
  <Route handler={AppBase} path="/">
    <DefaultRoute name="bird-list" handler={BirdList}/>
    <Route name="bird" path="/:bird_id" handler={BirdList}/>
    <NotFoundRoute handler={NotFound}/>
  </Route>
)


app_div = document.getElementById('react_app')


HistoryLocation = require 'react-router/lib/locations/HistoryLocation'


runRouter routes, HistoryLocation, (Handler) ->
  React.render(<Handler/>, app_div)
