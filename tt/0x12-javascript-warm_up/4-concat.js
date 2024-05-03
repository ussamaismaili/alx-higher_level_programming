#!/usr/bin/node
const { argv } = require('process');
const argValue1 = argv.slice(2)[0];
const argValue2 = argv.slice(3)[0];
console.log(argValue1, 'is', argValue2);
