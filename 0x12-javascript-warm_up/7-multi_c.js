#!/usr/bin/node

const arg = process.argv[2];
const num = parseInt(arg);
let i = 0;

if (typeof num !== 'number') {
  console.log('Missing number of occurrences');
}
while (i < num) {
  console.log('C is fun');
  i++;
}
