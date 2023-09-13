#!/usr/bin/node

// import the rect class from 5
const SquareA = require('./5-square');

// Define the square class that inherits from Square class
class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let k = '';
      for (let j = 0; j < this.width; j++) {
        k += c;
      }
      console.log(k);
    }
  }
}
module.exports = Square;
