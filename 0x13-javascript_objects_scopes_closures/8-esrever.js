#!/usr/bin/node
exports.esrever = function (list) {
  let first = 0;
  let last = list.length - 1;
  while (first < last) {
    const valHolder = list[first];
    list[first] = list[last];
    list[last] = valHolder;
    first++;
    last--;
  }
  return list;
};
