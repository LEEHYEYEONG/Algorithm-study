import sys
from collections import deque

n, m, v = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
  a, b = map(int,sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)
  graph[a].sort()
  graph[b].sort()

def DFS(node, graph, visited):
  visited[node] = True
  print(node, end=" ")
  for i in graph[node]:
    if not visited[i]:
      DFS(i, graph, visited)

def BFS(start,graph,visited):
  visited = [0 for _ in range(n+1)]
  queue = deque([start])
  visited[start] = True
  print(start,end=" ")
  while queue:
    node = queue.popleft()
    for i in graph[node]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        print(i,end=" ")


DFS(v,graph,visited)
print()
BFS(v,graph,visited)