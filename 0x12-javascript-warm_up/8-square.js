#!/usr/bin/node
const num = parseInt(process.argv[2]);
let i = 0;
let j = 0;

if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (i < num) {
    j = 0;
    while (j < num) {
      process.stdout.write('X');
      j++;
    }
    process.stdout.write('\n');
    i++;
  }
}
