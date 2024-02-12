#!/usr/bin/node
function factorial (argument) {
  if (argument < 0) {
    return (-1);
  }
  if (argument === 0 || isNaN(argument)) {
    return (1);
  }
  return (argument * factorial(argument - 1));
}

console.log(factorial(Number(process.argv[2])));
