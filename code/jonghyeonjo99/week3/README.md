# 1260 : DFS와 BFS
## 😎solved code
### 💻code
```python
import sys
from collections import deque

n, m, v = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
  a, b = map(int,sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)
  #정점 번호가 작은 것이 먼저 방문되기위해 sort
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
  ```
## ❗️결과
성공
## 💡접근
각각의 BFS, DFS 방식으로 탐색하는 함수를 정의하고 호출한다.
## 🧐문제 회고
오랜만에 Bact to basic으로 돌아가서 dfs, bfs 탐색을 생각해볼 수 있었다.
그래프를 순회하는 과정에서 gragh[node]의 원소를 기준으로 반복문을 돌리다보니, 정점 번호가 작은 것이 먼저 방문되기위해 그래프의 노드들을 sort해주어야함에 유의하자!

# 12851 : 숨바꼭질2
## 😎solved code
## 🥺unsolved code
### 💻code
```python

  ```
## ❗️결과

## 💡접근

## 🧐문제 회고

# 1234 : ABCD
## 😎solved code
## 🥺unsolved code
### 💻code
```python

  ```
## ❗️결과

## 💡접근

## 🧐문제 회고