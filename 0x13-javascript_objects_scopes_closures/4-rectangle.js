#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  // instance that uses X to print rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      let k = '';
      for (let j = 0; j < this.width; j++) {
        k += 'X';
      }
      console.log(k);
    }
  }

  // instance thst exchanges the width and height of the rect
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // instance that double the rec by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
