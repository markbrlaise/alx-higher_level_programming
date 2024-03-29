#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w * h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const swap = this.width;
    this.width = this.height;
    this.height = swap;
  }
}

module.exports = Rectangle;
