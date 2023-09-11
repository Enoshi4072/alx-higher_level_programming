#!/usr/bin/node
const arg = process.argv[2];
const intv = parseInt(arg, 10);
if (isNaN(intv)) {
  console.log('Not a number');
} else {
  console.log('My number: ', intv);
}
