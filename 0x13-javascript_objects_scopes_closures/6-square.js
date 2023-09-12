#!/usr/bin/node
const pSquare = require('./5-square');

class Square extends pSquare {
  charPrint (c = 'X') {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
