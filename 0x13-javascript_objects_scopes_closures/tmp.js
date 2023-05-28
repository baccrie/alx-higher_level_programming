#!/usr/bin/node

fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
let file_c = '';

fs.readFile(fileA, (err, file) => {
  file_c = file.toString();
  console.log(file_c);
});

fs.readFile(fileB, (err, file) => {
  file_c += file.toString();
  console.log(file_c);
});

fs.writeFile(fileC, file_c, { flag: 'a' }, 'utf-8');
