#!/usr/bin/node
// This script sets up a simple Express server that fetches
// data from the ALX Starwars API

const request = require('request');
const movieId = process.argv[2];
const mEndPoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function getRequest (characterList, index) {
  if (index >= characterList.length) {
    return;
  }

  request(characterList[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);
    } else {
      console.error('Error fetching character:', error);
    }
    getRequest(characterList, index + 1);
  });
}

request(mEndPoint, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterList = movie.characters;
    getRequest(characterList, 0);
  } else {
    console.error('Error fetching movie:', error);
  }
});
