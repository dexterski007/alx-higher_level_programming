#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieid = process.argv[2];

req(`${url}${movieid}/`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body).characters;
    printcharas(data, 0);
  }
});

function printcharas (characters, index) {
  req(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const json2 = JSON.parse(body).name;
      console.log(json2);
      if (index + 1 < characters.length) {
        printcharas(characters, index + 1);
      }
    }
  });
}
