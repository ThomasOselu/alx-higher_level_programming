#!/usr/bin/node

// a script that gets the contents of a webpage and writes file.
const fs = require('fs');
const rq = require('request');

function scrapeLoremIpsum (url, filePath) {
  rq.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}

const url = process.argv[2];
const filePath = process.argv[3];

scrapeLoremIpsum(url, filePath);
