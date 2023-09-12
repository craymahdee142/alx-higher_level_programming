#!/usr/bin/node

const argsList = process.argv.slice(2);
const numbers = argsList.map(arg => parseInt(arg));
if (numbers.length < 2) {
    console.log(0);
}else {
    const sortedNumbers = numbers.sort((a, b) => b - a);
    const secondLargest = sortedNumbers[1];
    console.log(secondLargest);
}
