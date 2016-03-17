var React = require("react");
var MaterialUI = require("material-ui")
//var MessageBoard = require("./components/MessageBoard");

//import React from 'react';
var ReactDOM = require("react-dom")
//import ReactDOM from 'react-dom';
var Main = require("./components/Main")
var RaisedButton = require('material-ui/lib/raised-button');
var injectTapEventPlugin = require("react-tap-event-plugin")
//import Main from './Main'; // Our custom react component
injectTapEventPlugin();
//React.render(<MaterialUI.AppBar/>,document.getElementById("message-board-container"));
//Main.js.render(<ProdcutGrid />, document.getElementById("message-board-container"));
var CommentBox = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        Hello, world! I am a CommentBox.
      </div>
    );
  }
});
ReactDOM.render(
  <Main />,
  document.getElementById('message-board-container')
);