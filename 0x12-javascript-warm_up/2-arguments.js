#!/usr/bin/node

const args = process.argv.slice(2); // Slice the first two elements
const count = args.length;

if (count === 0) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
