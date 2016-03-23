var React = require("react");
//var MaterialUI = require("material-ui")
var ReactDOM = require("react-dom")
var Main = require("./components/Main")
var injectTapEventPlugin = require("react-tap-event-plugin")
injectTapEventPlugin();

ReactDOM.render(
  <Main />,
  document.getElementById('message-board-container')
);