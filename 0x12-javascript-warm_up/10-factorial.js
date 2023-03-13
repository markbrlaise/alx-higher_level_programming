#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial (a) {
  if (a > 1) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}
if (num === undefined) {
  console.log(1);
} else {
  console.log(factorial(num));
}
