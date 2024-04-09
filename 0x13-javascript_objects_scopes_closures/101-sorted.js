#!/usr/bin/node
const dict = require('./101-data').dict;

const dict2 = {};

for (const [uid, occur] of Object.entries(dict)) {
  if (!dict2[occur]) {
    dict2[occur] = [];
  }
  dict2[occur].push(uid);
}

console.log(dict2);
