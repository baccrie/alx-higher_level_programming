#!/usr/bin/node

let arg = process.argv[2];
let num = parseInt(arg);
let i = 0;

if (typeof num != 'number') {
    console.log("Missing number of occurrences");
    return;
}
while (i < num) {
 console.log("C is fun");
 i++;
}
