#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request(args[0], function (error, response, body) {
  if (!error) {
    let result = {};
    const holder = JSON.parse(body);
    for (const iterator of holder) {
      console.log(iterator);
    }
  }
});