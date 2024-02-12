const input = require('fs').readFileSync('dev/stdin').toString().trim().split('\n');

const k = +input.shift().split(' ')[1];
const things = input.map(e => e.split(' ').map(v => +v));
const dp = new Array(k + 1).fill(0);

things.forEach((e) => {
    let [w, v] = e;
    for(let i = k; i >= w; i--){
        dp[i] = Math.max(dp[i], dp[i - w] + v);
    }
})

console.log(dp[k]);
