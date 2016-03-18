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
import CardActions from 'material-ui/lib/card/card-actions';
import CardHeader from 'material-ui/lib/card/card-header';
import CardMedia from 'material-ui/lib/card/card-media';
import CardTitle from 'material-ui/lib/card/card-title';
import FlatButton from 'material-ui/lib/flat-button';
import CardText from 'material-ui/lib/card/card-text';

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
    width:100,
  },
  dddd: {
    width : 600,
    margin:'0px auto',
    top: 200,
    position: 'relative',
  }
};

const tilesData = [
  {
    img: 'images/grid-list/00-52-29-429_640.jpg',
    title: 'Breakfast',
    author: 'jill111',
  },
  {
    img: 'images/grid-list/burger-827309_640.jpg',
    title: 'Tasty burger',
    author: 'pashminu',
  },
  {
    img: 'images/grid-list/camera-813814_640.jpg',
    title: 'Camera',
    author: 'Danson67',
  },
  {
    img: 'images/grid-list/morning-819362_640.jpg',
    title: 'Morning',
    author: 'fancycrave1',
  },
  {
    img: 'images/grid-list/hats-829509_640.jpg',
    title: 'Hats',
    author: 'Hans',
  },
  {
    img: 'images/grid-list/honey-823614_640.jpg',
    title: 'Honey',
    author: 'fancycravel',
  },
  {
    img: 'images/grid-list/vegetables-790022_640.jpg',
    title: 'Vegetables',
    author: 'jill111',
  },
  {
    img: 'images/grid-list/water-plant-821293_640.jpg',
    title: 'Water plant',
    author: 'BkrmadtyaKarki',
  },
];

const tableData = [
  {
    name: 'John Smith',
    status: 'Employed',
    selected: true,
  },
  {
    name: 'Randal White',
    status: 'Unemployed',
  },
  {
    name: 'Stephanie Sanders',
    status: 'Employed',
    selected: true,
  },
  {
    name: 'Steve Brown',
    status: 'Employed',
  },
  {
    name: 'Joyce Whitten',
    status: 'Employed',
  },
  {
    name: 'Samuel Roberts',
    status: 'Employed',
  },
  {
    name: 'Adam Moore',
    status: 'Employed',
  },
];


var Main = React.createClass({

  getInitialState: function () {
    return{
      products:[],
      displayRowCheckbox: false
    }
  },


  componentDidMount: function () {

    console.log('got text');
    var result = fetch('/products');
    result.then(function(response) {
      console.log('1111got text');
      console.log('response', response);
      console.log('header', response.headers.get('Content-Type'));
      return response.json()
    })
        .then(json =>  {
      var products = json.result;
      console.log('got text', this);
      this.submitMessage(products);

    }).catch(function(ex) {
      console.log('failed', ex)
    });


    console.log('1111got text')

  },



  submitMessage : function (products) {
    //products.map( (row, index) => (
    //
    //    //console.log(row);
    //
    //if (row.is_operation)
    //{
    //  row.is_operation = 'operationing';
    //}
    //else
    //{
    //  row.is_operation = 'fail';
    //}
    //))

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
            <TableBody
                displayRowCheckbox={this.state.displayRowCheckbox}
                deselectOnClickaway={this.state.deselectOnClickaway}
                showRowHover={this.state.showRowHover}
                stripedRows={this.state.stripedRows}
            >
              {this.state.products.map( (row, index) => (
                  <TableRow key={index} selected={row.selected}>
                    <TableRowColumn>{row.name}</TableRowColumn>
                    <TableRowColumn>{row.is_operation}</TableRowColumn>
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
