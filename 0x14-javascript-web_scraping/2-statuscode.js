#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request(args[0], function (error, response) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }
  console.log('code: ' + response.statusCode);
});
