#!/usr/bin/node
if (process.argv.length === 3 && +process.argv[2]) {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      console.log('x'.replace(/(\r\n|\n|\r)/gm, ''))
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
