#!/usr/bin/node
// a script that prints a message using the else if command depending of the number of arguments passed
if (process.argv.length === 2) {
    console.log('No argument');
  } else if (process.argv.length === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
