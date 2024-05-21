#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filepath, string, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
