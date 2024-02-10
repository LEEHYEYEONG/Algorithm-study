const input = require('fs').readFileSync('example.txt').toString().trim().split(' ');

const [n, k] = input.map(e => +e);
const dp = [];
for(let i = 0; i < k + 1; i ++){
   dp[i] = new Array(n + 1).fill(1);
}

for(let i = 2; i < k + 1; i++){
    for(let j = 1; j < n + 1; j++){
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000;
    }
}

console.log(dp[k][n])