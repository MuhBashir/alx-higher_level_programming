#!/usr/bin/node
const file_system = require('fs');
const a_b = file_system.readFileSync(process.argv[2], 'utf8');
const a_c = file_system.readFileSync(process.argv[3], 'utf8');
file_system.writeFileSync(process.argv[4], a_b + a_c);
