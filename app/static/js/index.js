var React = require("react");
//var MaterialUI = require("material-ui")
var ReactDOM = require("react-dom")
var Main = require("./components/Main")
var injectTapEventPlugin = require("react-tap-event-plugin")
var Promise = require('es6-promise').Promise;
injectTapEventPlugin();

ReactDOM.render(
  <Main />,
  document.getElementById('message-board-container')
);