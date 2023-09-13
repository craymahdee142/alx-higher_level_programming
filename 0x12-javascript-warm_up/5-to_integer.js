#!/usr/bin/node

const argc2 = process.argv[2];
const parsedNumber = parseInt(argc2);

if (isNaN(parsedNumber)) {
  console.log('Not a number');
} else {
  console.log('My number:', parsedNumber);
}
