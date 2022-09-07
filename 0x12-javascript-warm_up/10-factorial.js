#!/usr/bin/node

const num = parseInt(process.argv[2]);
let fact = 1;
if (isNaN(num)) {
  console.log('1');
}
while (num !== 1) {
  fact *= num;
  num -= 1;
}
console.log(fact);