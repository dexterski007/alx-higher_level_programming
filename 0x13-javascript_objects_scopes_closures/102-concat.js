#!/usr/bin/node
const fs = require('fs');

const first = process.argv[2];
const second = process.argv[3];

const farg = fs.readFileSync(first.toString());
const sarg = fs.readFileSync(second.toString());

fs.writeFileSync(process.argv[4], farg + sarg);
