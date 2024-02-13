#!/usr/bin/node
exports.esrever = function (list) {
  let le = list.length - 1;
  let a = 0;
  while ((le - a) > 0) {
    const aux = list[le];
    list[le] = list[a];
    list[a] = aux;
    a++;
    le--;
  }
  return list;
};
