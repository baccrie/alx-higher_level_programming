#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('1');
} else {
  function fact (n) {
    if (n === 1) {
      return (n);
    } else {
      return (n * fact(n - 1));
    }
  }
  console.log(fact(num));
}
