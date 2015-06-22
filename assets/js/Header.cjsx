React = require('react')

Navbar = require('react-bootstrap/lib/Navbar')
Nav = require('react-bootstrap/lib/Nav')
NavItemLink = require('react-router-bootstrap/lib/NavItemLink')


Header = React.createClass
  render: ->
    <Navbar brand="Birdo" inverse fixedTop toggleNavKey={0}>
      <Nav right eventKey={0}>
        <NavItemLink eventKey={0} to="bird-list">Birds Overview</NavItemLink>
      </Nav>
    </Navbar>


module.exports = Header
