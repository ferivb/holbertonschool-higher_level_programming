#!/usr/bin/node
const args = process.argv.slice(2);

function nextBiggest (arr) {
  let max = -Infinity;
  let result = -Infinity;

  for (const value of arr) {
    const nr = Number(value);

    if (nr > max) {
      [result, max] = [max, nr]; // save previous max
    } else if (nr < max && nr > result) {
      result = nr; // new second biggest
    }
  }
  return result;
}
if (args[1]) {
  console.log(nextBiggest(args));
} else {
  console.log(0);
}
