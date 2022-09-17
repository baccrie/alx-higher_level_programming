#!/usr/bin/node
let result;
if (process.argv.length === 2) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('1');
} else if (process.argv.length > 3) {
  let total = process.argv.length + 2;
  let first = parseInt(process.argv[2]);
  let i = 2;
  let arr;
  let j = 0;

  while (i < total) {
    if (parseInt(process.argv[i]) > first) {
      first = parseInt(process.argv[i]);
    }
    arr[j] = process.argv[i];
    j++;
    i++;
}
j = 0;
i = 0;
while (i < arr.length) {
  if (arr[i] == first) {
    
console.log(first);
}
/**
if (process.argv.length < 4) {
  console.log('0');
} else {
  const data = process.argv.slice(2);
  data.sort((a, b) => b - a);
  console.log(data[1]);
  }
  **/
