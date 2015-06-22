React = require('react')

Grid = require 'react-bootstrap/lib/Grid'
Col = require 'react-bootstrap/lib/Col'
Row = require 'react-bootstrap/lib/Row'


MainContainer = React.createClass
  render: ->
    <Grid className="main-container">
      <Row>
        <Col xs={12} {...@props}>
          {@props.children}
        </Col>
      </Row>
    </Grid>


module.exports = MainContainer
