#!/usr/bin/node

fs = require('fs');

let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];
let file_c = "";

fs.readFile(fileA, (err, file) => {
  file_c = file.toString();
  console.log(file_c);
})

fs.readFile(fileB, (err, file) => {
  file_c += file.toString();
  console.log(file_c)
})

fs.writeFile(fileC, file_c, { flag: 'a' }, 'utf-8')