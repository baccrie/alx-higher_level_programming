#!/usr/bin/node

let first = parseInt(process.argv[2]);
if (!first) {
    console.log('Missing number of occurrences');
}
else {
    for (let i = 0; i < first; i++) {
        console.log('C is fun');
    }
}