import sys,heapq

N=int(sys.stdin.readline()) 
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0])

count = []
for i in range(N):
    if count and count[0] <= arr[i][0]:
        heapq.heappop(count)
    heapq.heappush(count, arr[i][1])

print(len(count))