import sys
n, k = map(int, sys.stdin.readline().split())
bag = [[0, 0]]
for i in range(n):
    bag.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = bag[i][0]
        value = bag[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
    

print(dp[n][k])

        