const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
input.shift(); // 주어진 N 버리고 사람 데이터만 남김

input.sort((a, b) => +a.split(' ')[0] - +b.split(' ')[0]); //나이로 비교

console.log(input.join('\n'));