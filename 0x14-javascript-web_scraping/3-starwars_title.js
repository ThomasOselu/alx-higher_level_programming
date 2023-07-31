#!/usr/bin/node

// prints the title of a Star Wars movie by movie ID
const rq = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

rq(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
