#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const string_to_write = process.argv[3];

fs.writeFile(filepath, string_to_write, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
