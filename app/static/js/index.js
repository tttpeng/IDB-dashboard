var React = require("react");
var MaterialUI = require("material-ui")
//var MessageBoard = require("./components/MessageBoard");

//import React from 'react';
var ReactDOM = require("react-dom")
//import ReactDOM from 'react-dom';

var injectTapEventPlugin = require("react-tap-event-plugin")
//import Main from './Main'; // Our custom react component

React.render(<MaterialUI.AppBar/>,document.getElementById("message-board-container"));
