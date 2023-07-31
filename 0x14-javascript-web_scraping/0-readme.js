#!/usr/bin/node

// reads and prints the content of a file; print error object if errors;
const fs = require('fs');

function readFile (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

const filePath = process.argv[2];
if (!filePath) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

readFile(filePath);
