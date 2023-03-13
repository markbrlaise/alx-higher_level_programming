#!/usr/bin/env node
if ((isNaN(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing number of ocurences');
} else {
  const size = parseInt(process.argv[2]);
  let i = 0;
  while (i < size) {
    console.log('C is fun');
    i++;
  }
}
