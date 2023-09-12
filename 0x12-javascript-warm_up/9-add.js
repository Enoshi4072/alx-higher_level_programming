#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const answer = parseInt(a) + parseInt(b);
    console.log(answer);
  }
}
const arg1 = process.argv[2];
const arg2 = process.argv[3];
add(arg1, arg2);
