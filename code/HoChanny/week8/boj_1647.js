const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input.shift().split(' ').map(Number);

const edges = input.map((e) => e.split(' ').map(Number)).sort((a, b) => a[2] - b[2]);

function getParent(x, parent) {
    if (parent[x] === x) return x;
    else return parent[x] = getParent(parent[x], parent);
}

const unionParent = (a, b, parent) => {
    a = getParent(a, parent);
    b = getParent(b, parent);
    if (a < b) {
        parent[b] = a;
    }
    else {
        parent[a] = b;
    }
}

const parent = new Array(n + 1).fill(0);
for (let i = 0; i < n + 1; i++) {
    parent[i] = i;
}

let result = 0;
let cnt = 0;

for (const edge of edges) {
    if (cnt === n - 2) break;
    const rootA = getParent(edge[0], parent);
    const rootB = getParent(edge[1], parent);
    const value = edge[2];

    if(rootA !== rootB) {
        unionParent(edge[0], edge[1], parent);
        result += value;
        cnt++;
    }
}

console.log(result);
