#!/usr/bin/node

function secondLargest (args) {
  if ((args.length === 0) || args.length === 1) {
    return 0;
  }
  let biggest = args[0];
  let secBig = null;
  let i = 0;
  for (i = 1; i < args.length; i++) {
    if (args[i] > biggest) {
      secBig = biggest;
      biggest = args[i];
    } else if (args[i] > secBig && args[i] !== biggest) {
      secBig = args[i];
    }
  }
  return secBig;
}
const args = process.argv.slice(2);
const answer = secondLargest(args);
console.log(answer);
