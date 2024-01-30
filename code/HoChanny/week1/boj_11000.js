const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = +inputData[0];
let timeTable = []; // 주어진 시간들을 저장할 배열
for (i = 1; i < n + 1; i++){
    let temp = inputData[i].split(' ').map((value) => +value);
    timeTable.push([temp[0], 1]); // [시작시간, 1]
    timeTable.push([temp[1], -1]); // [종료시간, -1]
}

timeTable = timeTable.sort((a, b)=> { // 시간순으로 정렬, 시간이 같다면 종료가 먼저 오게 정렬
    if(a[0] == b[0]){
        return a[1] - b[1]
    }
    else{
        return a[0] - b[0]
    }
})

let nowUsed = 0; // 현재 사용중
let result = 0; // 결과값(nowUsed의 최댓값)

timeTable.forEach((value) => {
    nowUsed += value[1];
    result = Math.max(result, nowUsed);
})

console.log(result);