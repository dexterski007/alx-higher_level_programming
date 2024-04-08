#!/usr/bin/node

const tabl = process.argv.slice(2).map(Number);

if (tabl.length < 2) {
  console.log(0);
} else {
  const sorted = tabl.sort((a, b) => b - a);
  console.log(sorted[1]);
}
