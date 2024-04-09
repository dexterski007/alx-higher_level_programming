#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);

const list2 = list.map((val, index) => (val * index));

console.log(list2);
