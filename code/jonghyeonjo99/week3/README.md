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
### 💻code
```python
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
visited = [0] * 100001

q = deque([(n, 0)])
fast, way = 10 ** 6, 0

while q:
  now, time = q.popleft()
  visited[now] = 1
  if now == k and time <= fast:
    fast = min(fast, time)
    way += 1
  if time > fast: break

  for x in (now - 1, now + 1, now * 2):
    if x in range(100001) and not visited[x]:
      q.append((x, time + 1))
  
print(fast)
print(way)
  ```
## ❗️결과
실패 후 참조
## 💡접근
1. 수빈이가 현재 위치에서 다음 위치로 갈 수 있는 방법은 현재위치가 x라 하면, x-1, x+1 x*2 세가지 방법이 있다.
2. 이를 그래프의 부모 자식 노드관계로 보고, BFS 탐색을 통해 수빈이가 동생의 위치까지 갈 수 있는 가장 빠른 시간은 루트노드인 수빈이의 위치에서 동생 위치 노드까지의 
깊이라 생각했다.
3. 그리고 동생의 위치까지 갈 수 있는 방법의 수는 최단 깊이에서 동생의 위치가 나왔을 때, 같은 깊이에 있는 또다른 동생의 위치 노드로 생각했다.

처음에 이러한 접근방식을 생각하여 문제를 풀었지만, 그래프가 어느 깊이까지 그려졌을 때, 원하는 값이 있을지 보장이 되지 않았다.
(문제 예시에서 동생의 위치가 17이였는데, 동생의 위치보다 더 멀리 갔다가 다시 걸어서 되돌아오는 경우)

결국 구글링을 통해 다른 풀이를 참조해보았습니다.

## 🧐문제 회고
BFS, DFS 탐색문제에서 그래프가 확정적이지 않은 문제를 처음만나 굉장히 당황했다..ㅠ
탐색과정에서 조건을 걸어 그래프를 순차적으로 탐색하는 방법에 대해 알아갈 수 있었다.

# 81302 : 거리두기 확인하기
## 😎solved code
### 💻code
```python
from collections import deque

def BFS(gragh):
	seats = [] # P좌표 모음
	for i in range(5):
		for j in range(5):
			if gragh[i][j] == 'P':
				seats.append([i,j])

	for x, y in seats:
		visited = [[0 for _ in range(5)] for _ in range(5)]
		distance = [[0 for _ in range(5)] for _ in range(5)]
		visited[x][y] = True
		queue = deque()
		queue.append([x,y])
		
		while queue:
			x_now, y_now = queue.popleft()
	
			#상 우 하 좌
			dx = [-1, 0, 1, 0]
			dy = [0, 1, 0, -1]

			for i in range(4):
				nx = x_now + dx[i]
				ny = y_now + dy[i]

				if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == 0:
                    
					if gragh[nx][ny] == 'O':
						queue.append([nx, ny])
						visited[nx][ny] = 1
						distance[nx][ny] = distance[x_now][y_now] + 1
                    
					elif gragh[nx][ny] == 'P' and distance[x_now][y_now] <= 1:
						return 0

	return 1

def solution(places):
	answer = []

	for i in places:
		answer.append(BFS(i))

	return answer
  ```
## ❗️결과
성공
## 💡접근
1. 우선 응사자들의 위치를 탐색 시작 위치로 선정하기 위해 'P'의 위치를 모두 수집한다.
2. 응시자 사이의 맨허튼거리는 응시자 사이의 최단거리를 의미하기 때문에, BFS를 이용하여 응시자 사이의 최단거리를 탐색한다.
3. 'O'는 빈 자리 이므로 응시자 사이의 거리가 연결되지만, 'X'는 파티션으로 막혀있기 때문에 탐색이 불가한 자리이다.
4. 응시자가 또다른 응시자 'P'를 만났을 때, distance가 2보다 작다면 0을 return해주고, 그렇지 않다면 거리두기가 잘 지켜진 것이기 때문에 1을 return한다.

## 🧐문제 회고
시작지점과 끝지점까지의 최단거리를 알아보기 위한 대표적인 BFS탐색 문제였다고 생각한다.
다만, 빈 테이블, 파티션, 응시자가 의미하는 바가 무엇인지 생각하는 과정이 필요한 문제였다.