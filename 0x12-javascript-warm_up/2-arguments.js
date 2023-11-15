#!/usr/bin/node
const { argv } = require('process');
(argv.length <= 2) ? console.log('No argument') : console.log('Argument found');
