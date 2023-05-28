#!/usr/bin/node

const req = require('request');
let result;

req(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const ob = {};
  result = JSON.parse(body);

  for (const i of result) {
    const v = i.userId;
    ob[v] = 0;
  }

  for (const i of result) {
    const v = i.userId;
    if (i.completed === true) {
      ob[v] += 1;
    }
  }

  console.log(ob);
});
