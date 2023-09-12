#!/usr/bin/node

function fact (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  }
  return (n * fact(n - 1));
}
const arg1 = process.argv[2];
const answer = fact(arg1);
console.log(answer);
