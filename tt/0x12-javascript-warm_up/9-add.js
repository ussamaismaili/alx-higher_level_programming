#!/usr/bin/node
const { argv } = require('process');
const a = argv.slice(2)[0];
const b = argv.slice(3)[0];
function add(a, b){
  console.log(parseInt(a) + parseInt(b));
}
add(a,b);
