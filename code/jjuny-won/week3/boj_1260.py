import sys
from collections import deque

def dfs(v):
    #방문 요소 = 1
    visited[v] = 1 
    print(v,end= ' ')
    for i in range(1,n+1):
        if graph[v][i] ==1 and visited[i] ==0:
            dfs(i)    
            
def bfs(v):
    queue=[v] #(deque[start])
    visited2[v]=1
    while queue:
        v  = queue.pop(0)
        print(v,end=' ')
        for i in range(1,n+1):
            if (graph[v][i]==1 and visited2[i]==0):
                queue.append(i)
                visited2[i] =1

#입력받는 부분
n,m,v = map(int,input().split())

#행렬 만들기
graph = [[0]*(n+1) for _ in range(n+1)]


for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
    

#방문 리스트 만들기
visited = [0]*(n+1)
visited2 = [0]*(n+1)
dfs(v)
print()
bfs(v)


