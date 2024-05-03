#!/usr/bin/node
const { argv } = require('process');
const argValue = argv.slice(2)[0];
if (isNaN(argValue)){
    console.log('Missing size'); 
  } else {
  const myStr = 'X'.repeat(argValue);
  for (let i = 0;i < argValue; i++){
    console.log(myStr);
  } 
}
