#!/usr/bin/env node

// import { argv } from 'node:process';

if (process.argv.length === 2) {
  console.log('No Argument found');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
