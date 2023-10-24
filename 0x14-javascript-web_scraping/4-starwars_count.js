#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  // Added error handling for the request
  if (error) {
    console.error(error);
    process.exit(1);
  }

  const data = JSON.parse(body);
  const wedgeAntillesID = 18;

  // Added check for valid data format
  if (!data.results) {
    console.error('Invalid data format');
    process.exit(1);
  }

  // Filter movies based on characters including Wedge Antilles
  const moviesWithWedgeAntilles = data.results.filter(movie =>
    movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesID}/`)
  );

  console.log(moviesWithWedgeAntilles.length);
});
