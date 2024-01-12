const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = +inputData[0];
const target = +inputData[1];


const board = new Array(n).fill().map(() => new Array(n).fill(0));

let startX = Math.floor(n / 2); // 1을 정중앙에 넣는 과정
let startY = Math.floor(n / 2);
let targetCoordination = [startX + 1, startY + 1];
board[startX][startY] = 1;

let count = 2; // 첫 테두리의 시작인 2부터 넣을 것임
startY += 1; // 2의 위치를 위한 조정

for (let i = 1; i < Math.floor(n / 2) + 1; i++) {
    startX -= 1; // 각 테두리의 시작점 설정
    startY -= 1;

    if (count == target) targetCoordination = [startX + 1, startY + 1]; // 주어진 정수가 현재 정수인지 체크
    board[startX][startY] = count++;
    let nowX = startX;
    let nowY = startY;
    

    for (let r = 0; r < i * 2 - 1; r++) { //오른쪽으로 이동
        nowY += 1;
        board[nowX][nowY] = count;
        if (count == target) targetCoordination = [nowX + 1, nowY + 1];
        count++;
    }

    for (let d = 0; d < i * 2; d++) { //아래로 이동
        nowX += 1;
        board[nowX][nowY] = count;
        if (count == target) targetCoordination = [nowX + 1, nowY + 1];
        count++;
    }

    for (let l = 0; l < i * 2; l++) { //왼쪽으로 이동
        nowY -= 1;
        board[nowX][nowY] = count;
        if (count == target) targetCoordination = [nowX + 1, nowY + 1];
        count++;
    }

    for (let u = 0; u < i * 2; u++) { //위로 이동
        nowX -= 1;
        board[nowX][nowY] = count;
        if (count == target) targetCoordination = [nowX + 1, nowY + 1];
        count++;
    }
}

for (let i = 0; i < n; i++) {
    console.log(board[i].join(' '));
}
console.log(targetCoordination.join(' '));
