N, K = map(int,input().split())
answer = 1
dp = [[0]*(N+1) for _ in range(K+1)]
for i in range(K+1):
    for j in range(N+1):
        if i == 1:
            dp[i][j] = 1
        elif i == 2:
            dp[i][j] = j+1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
answer = max(dp[K])
print(answer % 1000000000)



