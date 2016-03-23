/**
 * In this file, we create a React component
 * which incorporates components providedby material-ui.
 */

import React from 'react';
import Table from 'material-ui/lib/table/table';
import TableHeaderColumn from 'material-ui/lib/table/table-header-column';
import TableRow from 'material-ui/lib/table/table-row';
import TableHeader from 'material-ui/lib/table/table-header';
import TableRowColumn from 'material-ui/lib/table/table-row-column';
import TableBody from 'material-ui/lib/table/table-body';
import TableFooter from 'material-ui/lib/table/table-footer';
import TextField from 'material-ui/lib/text-field';
import Toggle from 'material-ui/lib/toggle';
import Card from 'material-ui/lib/card/card';
import es6promise from 'es6-promise';

es6promise.polyfill();




const styles = {
  propContainerStyle: {
    width: 200,
    overflow: 'hidden',
    margin: '20px auto 0',
  },
  propToggleHeader: {
    margin: '20px auto 10px',
  },
  tableRowColum: {
    width: 100,
    backgroundColor: '#ff123f',
  },
  tables: {
    backgroundColor: '#fff',
  },
  dddd: {
    width: '760px',
    margin: '0 auto',
    top: 200,
    position: 'relative',
  }
};


var Main = React.createClass({

  getInitialState: function () {
    return {
      products: [],
      displayRowCheckbox: false,
      adjustForCheckbox: false
    }
  },



    handleResize: function(e) {
      console.log('handResize');

      let el = React.findDOMNode(this);
      console.log(window.innerWidth);
      console.log(window.screen.width);

      el.style.width = window.innerWidth;
  },

  componentDidMount: function () {
    //window.addEventListener('resize', this.handleResize);
    var result = fetch('/products');
    result.then(function (response) {
        console.log('1111got text');
        console.log('response', response);
        console.log('header', response.headers.get('Content-Type'));
        return response.json()
      })
      .then(json => {
        var products = json.result;
        console.log('got text', this);
        this.submitMessage(products);

      }).catch(function (ex) {
      console.log('failed', ex)
    });


    console.log('1111got text')

  },


  submitMessage: function (products) {

    this.setState({
      products: products
    });
  },

  render() {


    return (
      <Card style={styles.dddd}>
        <Table
          style={styles.tables}
          height={this.state.height}
          fixedHeader={this.state.fixedHeader}
          fixedFooter={this.state.fixedFooter}
          selectable={this.state.selectable}
          multiSelectable={this.state.multiSelectable}
          onRowSelection={this._onRowSelection}
        >
          <TableHeader
            //style={styles.tables}
            displaySelectAll={this.state.adjustForCheckbox}
            adjustForCheckbox={this.state.adjustForCheckbox}>
            <TableRow>
              <TableHeaderColumn colSpan="3" tooltip="Super Header" style={{textAlign: 'center',fontSize:20}} >
                IDB Dashboard
              </TableHeaderColumn>
            </TableRow>
            <TableRow>
              <TableHeaderColumn tooltip="产品名称">产品名称</TableHeaderColumn>
              <TableHeaderColumn tooltip="运行状态">运行状态</TableHeaderColumn>
              <TableHeaderColumn tooltip="最后更新时间">最后更新时间</TableHeaderColumn>
            </TableRow>
          </TableHeader>
          <TableBody
            displayRowCheckbox={this.state.displayRowCheckbox}
            deselectOnClickaway={this.state.deselectOnClickaway}
            showRowHover={this.state.showRowHover}
            stripedRows={this.state.stripedRows}
          >
            {this.state.products.map((row, index) => (
              <TableRow key={index} selected={row.selected}>
                <TableRowColumn>{row.name}</TableRowColumn>
                <TableRowColumn style={{
                color:this.state.products[index].is_operation == 'operation' ? '#7ed321':'#ff123f'
                }}>{row.is_operation}</TableRowColumn>
                <TableRowColumn>{row.updateTime}</TableRowColumn>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Card>
    );
  }


});

module.exports = Main

//export default Main;
