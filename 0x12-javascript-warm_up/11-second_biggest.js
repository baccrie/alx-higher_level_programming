#!/usr/bin/node

const num = process.argv;
let biggest = 0;
let i = 2;
const len = num.length;

while (i < len) {
  if (parseInt(num[i]) >= biggest) {
    biggest = parseInt(num[i]);
  }
  // console.log(biggest);
  i++;
}

let secondBiggest = 0;
i = 2;

while (i < len) {
  if (parseInt(num[i]) >= secondBiggest & parseInt(num[i]) !== biggest) {
    secondBiggest = parseInt(num[i]);
  }
  // console.log(biggest);
  i++;
}

if (num.length === 2) {
  secondBiggest = 0;
}
console.log(secondBiggest);
