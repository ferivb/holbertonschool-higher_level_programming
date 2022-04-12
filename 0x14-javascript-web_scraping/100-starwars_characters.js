#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request('https://swapi-api.hbtn.io/api/films/' + args[0] + '/', function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }
  // console.log('statusCode:', response && response.statusCode); // Ion need this for now.
  const holder = JSON.parse(body);
  for (const chars of holder.characters) {
    request(chars, function (error, response, body) {
      if (!error) {
        const charHolder = JSON.parse(body);
        console.log(charHolder.name);
      }
    });
  }
});
