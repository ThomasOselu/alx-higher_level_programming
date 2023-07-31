#!/usr/bin/node

// prints all characters of a Star Wars movie in the right order
const req = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

req(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const charactersUrls = JSON.parse(body).characters;
    printCharactersNames(charactersUrls, 0);
  }
});

function printCharactersNames (charactersUrls, index) {
  if (index >= charactersUrls.length) {
    return;
  }

  req(charactersUrls[index], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const characterName = JSON.parse(body).name;
      console.log(characterName);
      printCharactersNames(charactersUrls, index + 1);
    }
  });
}
