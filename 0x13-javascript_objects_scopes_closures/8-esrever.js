#!/usr/bin/node
exports.esrever = function (list) {
  const revlist = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    revlist[j] = list[i];
    j++;
  }
  return revlist;
};
