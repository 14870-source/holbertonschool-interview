#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    return;
  }

  const movie = JSON.parse(body);

  const getCharacters = (characters, index) => {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (err, res, data) => {
      if (!err && res.statusCode === 200) {
        const character = JSON.parse(data);
        console.log(character.name);
      }

      getCharacters(characters, index + 1);
    });
  };

  getCharacters(movie.characters, 0);
});
