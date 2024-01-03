#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
const episodeNumber = process.argv[2];
const requestURL = 'http://swapi.co/api/films/' + episodeNumber;

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characterList = JSON.parse(body).characters;
    for (const characterURL in characterList) {
      request(characterList[characterURL],
        function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            const name = JSON.parse(body).name;
            console.log(name);
          }
        });
    }
  }
});
