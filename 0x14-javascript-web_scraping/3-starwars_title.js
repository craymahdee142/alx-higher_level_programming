#!/usr/bin/node

// import request module
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if {response.statusCode === 200) {
    const responseJSON = JSON.parse(bdy);
    console.log(responseJSON.title);
 } else {
  console.log('Error code: ' + response.statusCode);
 }
});
