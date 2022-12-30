#!/usr/bin/node
let sec;
let i = 2;
const len = process.argv.length;
const arr = [];

if (len < 3) {
  sec = 0;
} else if (len === 3) {
  sec = 0;
} else {
  let j = 0;
  while (i < len) {
    arr[j] = process.argv[i];
    i++;
    j++;
  }
  arr.sort();
  const leng = arr.length - 2;
  sec = arr[leng];
}
console.log(sec);
