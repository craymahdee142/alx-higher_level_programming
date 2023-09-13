#!/usr/bin/node

// import the rect class from 4
const Rectangle = require('./4-rectnagle');

// Define the square class that inherits from rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
