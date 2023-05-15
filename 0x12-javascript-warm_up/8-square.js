#!/usr/bin/node

const first = parseInt(process.argv[2]);
const second = first;
const text = 'X';
if (!first) {
  console.log('Missing size');
} else {
  for (let i = 0; i < first; i++) {
    console.log(text.repeat(first));
  }
}
