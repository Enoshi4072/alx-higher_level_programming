#!/usr/bin/node

let i = 0;
const x = process.argv[2];
const intv = parseInt(x, 10);
if (isNaN(intv)) {
  console.log('Missing number of occurrences');
}

for (i = 0; i < intv; i++) {
  console.log('C is fun');
}
