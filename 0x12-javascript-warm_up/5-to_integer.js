#!/usr/bin/node
const arg = process.argv[2];
const intv = parseInt(arg, 10);
if (!isNaN(intv)) {
  console.log('My number: ', intv);
} else {
  console.log('Not a number');
}
