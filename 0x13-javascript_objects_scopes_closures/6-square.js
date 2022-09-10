#!/usr/bin/node
const Sq = require('./5-square');
class Square extends Sq {
  charPrint (c) {
    let a;
    if (c === undefined) {
      a = 'X';
    } else {
      a = c;
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(a);
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Square;
