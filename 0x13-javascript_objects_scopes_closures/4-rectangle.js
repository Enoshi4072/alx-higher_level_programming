#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
	rotate () {
		const valueHold = this.width;
		this.width = this.height;
		this.height = valueHold;
	}
	double () {
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
}
module.exports = Rectangle;
