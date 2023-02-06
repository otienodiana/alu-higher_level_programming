#!usr/bin/node
//Iam writing a script for reading my json file
const fs = request('fs');
fs.readFile(process.arg[2],'utf8',function(error,content) {
    console.log(error|| content);
});