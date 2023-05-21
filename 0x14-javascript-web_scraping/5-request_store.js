#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const content = body.toString();
  // console.log(content)
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
