#!/usr/bin/node
if (process.argv[1]) {
  console.log('No argument');
} else if (process.argv[2]) {
  console.log(`${process.argv[2]}`);
}
