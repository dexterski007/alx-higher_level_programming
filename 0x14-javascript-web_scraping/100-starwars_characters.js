#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieid = process.argv[2];

req(`${url}${movieid}/`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonfile = JSON.parse(body);
    const charas = jsonfile.characters;
    for (const item of charas) {
        req.get(item, (error, response, body1) => {
          if (error) {
            console.error(error);
          }
          const data = JSON.parse(body1);
          console.log(data.name);
        });
      }
    }
  });
