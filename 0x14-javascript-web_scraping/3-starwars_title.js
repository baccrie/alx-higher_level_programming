#!/usr/bin/node

const request = require('request');
const epis = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(epis, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
}
);


