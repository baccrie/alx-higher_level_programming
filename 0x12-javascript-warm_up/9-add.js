#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
let sum;

function add (a, b) {
  sum = a + b;
  console.log(sum);
}
add(a, b);
