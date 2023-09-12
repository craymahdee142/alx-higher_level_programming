#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const argc2 = parseInt(process.argv[2]);
const argc3 = parseInt(process.argv[3]);
const sum = add(argc2, argc3);
console.log(sum);
