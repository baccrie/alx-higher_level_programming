#!/usr/bin/node

const num = process.argv;
let biggest = 0;
let i = 2;
const len = process.argv.length;

while (i < len) {
  if (process.argv[i] >= biggest) {
    biggest = process.argv[i];
  }
  console.log(biggest);
  i++;
}

if (process.argv[i] >= biggest) {
  biggest = process.argv[i];
}
// console.log(biggest);
