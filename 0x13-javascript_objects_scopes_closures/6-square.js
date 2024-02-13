#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      let sqr = '';
      for (let b = 0; b < this.width; b++) {
        sqr += c;
      }
      console.log(sqr);
    }
  }
}

module.exports = Square;
