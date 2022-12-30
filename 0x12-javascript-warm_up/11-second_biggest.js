#!/usr/bin/node
let sec;
let i = 2;
const len = process.argv.length;

if (len < 3) {
  sec = 0;
} else if (len === 3) {
  sec = 0;
} else {
  const arr = [];
  let j = 0;
  while (i < len) {
    arr[j] = process.argv[i];
    i++;
    j++;
  }
  arr.sort();
  sec = arr[1];
}
console.log(sec);
