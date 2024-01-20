const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
const [N, M, V] = input[0].split(' ').map(Number);
const edges = input.slice(1).map(line => line.split(' ').map(e => +e));

function dfs(graph, start, visited) {
    visited[start] = true;
    process.stdout.write(start + ' ');

    for (const nextNode of graph[start]) {
        if (!visited[nextNode]) {
            dfs(graph, nextNode, visited);
        }
    }
}

function bfs(graph, start) {
    const visited = Array(N + 1).fill(false);
    const queue = [start];
    visited[start] = true;

    while (queue.length) {
        const currentNode = queue.shift();
        process.stdout.write(currentNode + ' ');

        for (const nextNode of graph[currentNode]) {
            if (!visited[nextNode]) {
                visited[nextNode] = true;
                queue.push(nextNode);
            }
        }
    }
}

function solution(N, edges, V) {
    const graph = Array.from({ length: N + 1 }, () => []);

    for (const edge of edges) {
        const [u, v] = edge;
        graph[u].push(v);
        graph[v].push(u);
    }

    for (const neighbors of graph) {
        neighbors.sort((a, b) => a - b);
    }

    const visited = Array(N + 1).fill(false);
    dfs(graph, V, visited);
    console.log();

    bfs(graph, V);
    console.log();
}

solution(N, edges, V);
