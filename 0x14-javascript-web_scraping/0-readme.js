#!/usr/bin/node

const fs = require('fs');

// Get the path from command line argv
const filePath = process.argv[2];

// Read content of the file in utf-8
fs.readFile(filePath, 'utf8', (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
