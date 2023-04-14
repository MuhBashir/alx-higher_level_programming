#!/usr/bin/node
const file_system = require('fs');
const a = file_system.readFileSync(process.argv[2], 'utf8');
const b = file_system.readFileSync(process.argv[3], 'utf8');
file_system.writeFileSync(process.argv[4], a + b);
