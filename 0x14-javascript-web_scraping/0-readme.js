#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log(response);
  }
});
