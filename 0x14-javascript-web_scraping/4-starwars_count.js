#!/usr/bin/node

// prints the number of movies where the character "Wedge Antilles" is present
const req = require('request');

const apiUrl = process.argv[2];

req(apiUrl, (err, res, body) => {
  if (!err) {
    const movies = JSON.parse(body).results;
    console.log(movies.reduce((count, movie) => {
      return movie.characters.find((cha) => cha.endsWith('/18/')) ? count + 1 : count;
    }, 0));
  }
});
