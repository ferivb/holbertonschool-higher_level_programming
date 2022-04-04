#!/usr/bin/node
const args = process.argv;
function factorial (x) {
  if (x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
if (isNaN(parseInt(args[2]))) {
  console.log(1);
} else {
  console.log(factorial(parseInt(args[2])));
}
