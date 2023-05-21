#!/usr/bin/node

const request = require('request');
let count = 0;
const epis = process.argv[2];
request(epis, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const obj = JSON.parse(body).results;
  for (const li of obj) {
    if (li.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
}
);
