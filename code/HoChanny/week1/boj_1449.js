const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let l = + inputData[0].split(' ')[1];
let inputLocation = inputData[1].split(' ').map((value) => +value).sort((a,b) => a - b); // 오름차순 정렬

let result = 0; // 테이프의 개수
let temp = -1; // 테이프의 끝점

inputLocation.forEach((value) => {
    if(value > temp){
        result += 1;
        temp = value + l - 1;
    }
})

console.log(result);
