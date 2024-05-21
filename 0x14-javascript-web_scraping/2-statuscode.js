#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
