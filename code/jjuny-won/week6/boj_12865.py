import sys

N,K = map(int,input().split())
items = []
for _ in range(N):
    w,v = map(int,input().split())
    items.append((w,v))
    

dp = [0 for _ in range(K+1)] #최대 가치를 구하기 위한 일차원 배열


for item in items:
    w,v = item
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v) 
        #물건을 추가하기전 최대 가치와, 물건을 추가하고 난 후 최대 가치 비교해서 가치 업데이트
print(dp[-1])