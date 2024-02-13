#!/usr/bin/node
let totalArguments = 0;

exports.logMe = function (item) {
  console.log(totalArguments + ': ' + item);
  totalArguments++;
};
