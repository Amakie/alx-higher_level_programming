#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const episodeNumber = process.argv[2];
const requestURL = 'https://swapi-api.alx-tools.com/api/films/:id' + episodeNumber;

request(requestURL, function (error, response, body) {
  const theBody = JSON.parse(body);
  console.log(theBody.title);
  if (error) {
    console.log(error);
  }
});
