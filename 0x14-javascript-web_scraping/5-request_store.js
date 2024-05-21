#!/usr/bin/node
const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

req(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filepath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
