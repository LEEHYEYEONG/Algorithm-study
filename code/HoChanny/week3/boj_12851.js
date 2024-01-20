const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');
const [start, target] = input.map(e => +e);

let max = 100001;

let answer = new Array(max).fill(0); // 각 노드까지 도달할 수 있는 가짓수
let visited = new Array(max).fill(-1); // -1이면 방문 안함, 이외의 숫자는 각 노드에 도달할 수 있는 최소 시간
let q = [];

const getNextPos = (x, i) => { // x번 노드에서 방문할 수 있는 다음 노드는 x * 2, x + 1, x - 1번 노드이다.
    if (i == 0) return x * 2;
    else if (i == 1) return x + 1;
    else return x - 1;
}

visited[start] = 0;
answer[start] = 1;
q.push(start);

while(q.length){
    let currentPos = q.shift();

    for(let i = 0; i < 3; i ++){
        let nextPos = getNextPos(currentPos, i);
        
        if(nextPos >= max || nextPos < 0) continue;

        if(visited[nextPos] === -1){ // 첫 방문
            q.push(nextPos);
            visited[nextPos] = visited[currentPos] + 1; // 최단경로의 길이는 이전 노드까지의 경로의 길이 + 1
            answer[nextPos] += answer[currentPos]; // 현재까지 파악 가능한 최단경로는 이전노드에서 온 것 하나이고, 가짓수는 이전 노드까지의 최단 경로의 가짓수가 될 것이다.
        }
        else if(visited[nextPos] === visited[currentPos] + 1){ // 다른 최단 경로
            answer[nextPos] += answer[currentPos]; // 첫 방문시와 다른 노드에서 오는 최단경로가 생겼으므로, 그 노드까지의 최단 경로의 개수를 더해준다.
        }
    }
}

console.log(visited[target]);
console.log(answer[target]);