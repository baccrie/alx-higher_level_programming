#!/usr/bin/node

const req = require('request');
let result;

req(process.argv[2], (err, res, body) => {
  ob = {};
  result = JSON.parse(body);

  console.log(ob);
  // console.log(JSON.parse(body))
});
