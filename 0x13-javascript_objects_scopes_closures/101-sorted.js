#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

// iterate over the keys in the original dict
Object.keys(dict).map(function (key) {
  /// check is the value in the new dict is not an array
  if (!Array.isArray(newDict[dict[key]])) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
  return key;
});
console.log(newDict);
