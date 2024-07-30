#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    const getCharacter = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            resolve(JSON.parse(charBody).name);
          }
        });
      });
    };

    const fetchCharacters = async () => {
      for (const characterUrl of characters) {
        try {
          const characterName = await getCharacter(characterUrl);
          console.log(characterName);
        } catch (err) {
          console.error(err);
        }
      }
    };

    fetchCharacters();
  }
});
