#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonfile = JSON.parse(body);
    const completedtasks = {};
    jsonfile.forEach(item => {
      if (item.completed) {
        if (!completedtasks[item.userId]) {
          completedtasks[item.userId] = 0;
        }
        completedtasks[item.userId] += 1;
      }
    });
    console.log(completedtasks);
};
});
