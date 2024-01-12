const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const board = inputData[1].split(' ').map((e) => +e);

let result = 0;

for(let i = 0; i < board.length; i++){
    let leftPillar = Math.max(...board.slice(0, i)); // 왼쪽에서 가장 높은 기둥 찾기
    let rightPillar = Math.max(...board.slice(i + 1)); // 오른쪽에서 찾기
    let standard = Math.min(leftPillar, rightPillar); // 둘 중 작은 값이 물이 고이는 최고 높이가 될 것이다

    if(board[i] < standard){
        result += standard - board[i];
    }
}

console.log(result);