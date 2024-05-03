#!/usr/bin/node
const { argv } = require('process');
const argValue = argv.slice(2)[0];
const myString = "My number: ";
isNaN(argValue) ? console.log('Not a number') : console.log(myString + parseInt(argValue));
