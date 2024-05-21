#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
const id = '18';

req(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonfile = JSON.parse(body);
    const filmcounter = jsonfile.results.reduce((count, film) => {
      if (film.characters.some(character => character.endsWith(`/${id}/`))) {
        return count + 1;
      }
      return count;
    }, 0);
    console.log(filmcounter);
  }
});
