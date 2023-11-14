#!/usr/bin/node
let myargv = 0;
for (; process.argv[myargv]; myargv++) {
  if (myargv === 2) {
    console.log('No argument');
  } else {
    console.log(process.argv[2]);
  }
}
