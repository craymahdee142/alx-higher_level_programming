#!/usr/bin/node

const argc2 = process.argv[2];
const x = parseInt(argc2);

if (isNaN(x)) {
	console.log("Missing number of occurances");
}else {
	for (let i = 0; i < x; i++) {
		console.log("C is fun");
	}
}
