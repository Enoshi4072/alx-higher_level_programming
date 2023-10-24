#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  const data = JSON.parse(body);
  const wedgeAntillesID = 18;

  const moviesWithWedgeAntilles = data.results.filter(movie =>
    movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesID}/`)
  );

  console.log(moviesWithWedgeAntilles.length);
});
