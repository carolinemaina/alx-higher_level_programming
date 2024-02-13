#!/usr/bin/node

exports.converter = function (base) {
  return function (givenNumber) {
    return givenNumber.toString(base);
  };
};
