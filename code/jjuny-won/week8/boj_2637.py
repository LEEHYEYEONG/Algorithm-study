import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
result = [[0] * (n+1) for _ in range(n+1)]  #개수 저장할 배열

q = deque()
indegree = [0] * (n + 1)

for _ in range(m):
    a,b,c =map(int,input().split())
    graph[b].append((a,c))
    indegree[a] +=1

# print(graph)
def topology_sort():
    for i in range(1,n+1):
        if indegree[i] ==0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for nxt,cnt in graph[now]:
            if result[now].count(0)==n+1:
                result[nxt][now]+=cnt
            else:
                for i in range(n+1):
                    result[nxt][i] +=result[now][i]*cnt
            indegree[nxt] -=1
            if indegree[nxt] ==0:
                q.append(nxt)


    for parts in enumerate(result[n]):
        if parts[1]>0:
            f,c = parts
            print(f, c)     
topology_sort()