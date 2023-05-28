#!/usr/bin/node

fs = require('fs');

fileA = process.argv[2];
fileB = process.argv[3];
fileC = process.argv[4];
let cont = '';

fs.readFile(fileA, 'utf-8', (err, data) => {
  cont += data;
  fs.readFile(fileB, 'utf-8', (err, data) => {
    cont += data;
    console.log(cont);
    fs.writeFile(fileC, cont, err => {
      if (err) {
        console.log(err);
      }
    });
  });
});
