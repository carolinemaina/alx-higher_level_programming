#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const searchNum = process.argv.slice(2).map(Number);
  const secondNum = searchNum.sort(function (a, b) { return b - a; })[1];
  console.log(secondNum);
}
