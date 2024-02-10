function solution(N, number) {
    const dp = new Array(9).fill().map(_ => new Set());
    for(let i = 1; i < 9; i++){
        dp[i].add(+`${N}`.repeat(i));
        
        for(let j = 1; j < i; j++){
            for(x of dp[j].keys()){
                for(y of dp[i - j].keys()){
                    dp[i].add(x + y);
                    dp[i].add(x - y);
                    dp[i].add(x * y);
                    dp[i].add(Math.round(x / y));
                }
            }
        }

        if(dp[i].has(number)) return i;
    }
    return -1;
}

