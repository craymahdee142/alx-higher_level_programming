#!/usr/bin/node

const fs = require('fs');

// Get the path from command line
const filePath = process.argv[2];
// Read the file in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
