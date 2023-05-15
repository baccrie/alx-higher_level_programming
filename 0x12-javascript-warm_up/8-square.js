#!/usr/bin/node

let first = parseInt(process.argv[2]);
let second = first
let text = 'X';
if (!first) {
    console.log('Missing size');
}
else {
    for (let i = 0; i < first; i++) {
        console.log(text.repeat(first))
    }
}
