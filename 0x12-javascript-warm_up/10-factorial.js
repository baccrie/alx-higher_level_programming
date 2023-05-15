#!/usr/bin/node

const num = parseInt(process.argv[2]);
function factorial (no) {
  if (!no || no === 0 || no === 1) {
    return 1;
  }
  return factorial(no - 1) * no;
}

console.log(factorial(num));
