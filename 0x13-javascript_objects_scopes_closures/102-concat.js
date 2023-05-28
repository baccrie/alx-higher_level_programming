#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
let cont = '';

fs.readFile(fileA, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
  cont += data;
  fs.readFile(fileB, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
    cont += data;
    fs.writeFile(fileC, cont, err => {
      if (err) {
        console.log(err);
      }
    });
  });
});
