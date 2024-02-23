function solution(edges) {
    var answer = [0, 0, 0, 0];
    const degree = Array.from({length: 1000001}, () => [0, 0]);
    
    for(edge of edges){
        degree[edge[0]][0]++; // outdegree
        degree[edge[1]][1]++; // indegree
    }

    for(let i = 1; i <= 1000000; i++){
        const outD = degree[i][0];
        const inD = degree[i][1];

        if(outD - inD >= 2){
            answer[0] = i;
        }

        else if(outD === 0 && inD !== 0){ // 막대
            answer[2]++;
        }

        else if(outD >= 2 && inD >= 2){ //8자
            answer[3]++;
        }
    }

    answer[1] = degree[answer[0]][0] - answer[2] - answer[3];

    return answer;
}
