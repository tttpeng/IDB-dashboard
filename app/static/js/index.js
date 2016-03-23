var React = require("react");
//var MaterialUI = require("material-ui")
var ReactDOM = require("react-dom")
var Main = require("./components/Main")
var fetch = require('whatwg-fetch');
var injectTapEventPlugin = require("react-tap-event-plugin")
var Promise = require('es6-promise').Promise;
import es6promise from 'es6-promise';

es6promise.polyfill();
injectTapEventPlugin();

ReactDOM.render(
  <Main />,
  document.getElementById('message-board-container')
);