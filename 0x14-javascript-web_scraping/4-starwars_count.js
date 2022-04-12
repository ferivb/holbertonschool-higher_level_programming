#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request(args[0], function (error, response, body) {
  if (!error) {
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
  }
});
