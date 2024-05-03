#!/usr/bin/node
const { argv } = require('process');
const argValue = argv.slice(2)[0]; 
const myStr = 'C is fun';
if (isNaN(argValue)){
    console.log('Missing number of occurrences'); 
  } else {
  for (let i = 0;i < argValue; i++){
  console.log(`${myStr}`);
  } 
}
