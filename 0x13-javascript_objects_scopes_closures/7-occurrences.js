#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numElement = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      numElement++;
    }
  }
  return numElement;
};
