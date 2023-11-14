#!/usr/bin/node
const { argv } = require('process');
const argValue = argv.slice(2)[0];
(argValue !== undefined) ? console.log(argValue) : console.log('No argument');
