#!/usr/bin/node

const fs = require('fs');

function writeFile (filePath, writeString) {
  fs.writeFile(filePath, writeString, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

const filePath = process.argv[2];
const writeString = process.argv[3];

writeFile(filePath, writeString);
