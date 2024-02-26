const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = +input.shift();
const m = +input.shift();
const edges = input.map(_ => _.split(' ').map(Number));

const indegree = new Array(n + 1).fill(0);
const graph = Array.from({length : n + 1}, () => []);
const dp = Array.from({length : n + 1}, () => Array(n + 1).fill(0));

for(edge of edges){
    const [x, y, z] = edge;
    graph[y].push([x, z]);
    indegree[x]++;
}

const q = [];

for(let i = 1; i < n + 1; i++){
    if(indegree[i] === 0){
        q.push(i);
        dp[i][i] = 1;
    }
}

while(q.length){
    let now = q.shift();

    for(edge of graph[now]){
        let target = edge[0];
        let amount = edge[1];

        for(let i = 0; i < n + 1; i++){
            dp[target][i] += dp[now][i] * amount;
        }
        if(--indegree[target] === 0){
            q.push(target);
        }
    }
}

for(let i = 1; i < n; i++){
    if(dp[n][i] != 0){
        console.log(i, dp[n][i]);
    }
}