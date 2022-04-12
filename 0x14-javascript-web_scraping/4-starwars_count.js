#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request(args[0], function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  }
  // console.log('statusCode:', response && response.statusCode); // Ion need this for now.
  const holder = JSON.parse(body);
  const film = holder.results;
  let count = 0;
  for (const title of film) {
    const chars = title.characters;
    for (const search of chars) {
      if (search === 'https://swapi-api.hbtn.io/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});
