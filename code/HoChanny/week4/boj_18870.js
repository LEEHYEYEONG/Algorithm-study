const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let arr = input[1].split(' ').map(e => +e);
let sorted = [... new Set(arr)].sort((a, b) => a - b); //중복 제거 후 오름차순 정렬

let obj = {};
sorted.forEach((e, i) => {
    obj[e] = i;
})

console.log(arr.map(e => obj[e]).join(' '));