#!/usr/bin/node

let myVar = 89;

function modifyMyVar(newVar) {
    myVar = newVar;
}
modifyMyVar(333);
console.log(myVar);
