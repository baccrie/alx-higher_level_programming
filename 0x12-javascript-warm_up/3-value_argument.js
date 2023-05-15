#!/usr/bin/node

if (process.argv.length == 2) {
    console.log("No argument");
}
else {
    console.log(process.argv[2])
}
console.log(process.argv)
console.log(process.argv.length)