#!/usr/bin/node
let i = 0;
let j = 0;
const arg = process.argv[2];
const intv = parseInt(arg, 10);
if (isNaN(intv)) {
  console.log('Missing size');
} else {
  for (i = 0; i < intv; i++) {
    let oneRow = '';
    for (j = 0; j < intv; j++) {
      oneRow += 'X';
    }
    console.log(oneRow);
  }
}
