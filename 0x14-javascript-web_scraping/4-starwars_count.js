#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let sum = 0;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  response = JSON.parse(body).results;
  for (const i of response) {
    if (i.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      sum++;
    }
  }
  console.log(sum);
  // console.log(res);
});
