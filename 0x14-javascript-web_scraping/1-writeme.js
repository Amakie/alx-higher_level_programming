#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');
const fileName = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(fileName, stringToWrite, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
