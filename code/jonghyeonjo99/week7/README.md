# 1753 : 최단경로
## 😎solved code
### 💻code
```python
import sys
import heapq


INF = int(1e9)

V,E = map(int,sys.stdin.readline().rstrip().split())
k = int(sys.stdin.readline().rstrip())
node = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
queue = []

for i in range(E):
  u,v,w = map(int,sys.stdin.readline().rstrip().split())
  node[u].append((v,w))

heapq.heappush(queue,(0,k))
distance[k] = 0

while queue:
  dist, now = heapq.heappop(queue)

  if distance[now] < dist:
    continue

  for i in node[now]:
    cost = dist + i[1]
    if cost < distance[i[0]]:
      distance[i[0]] = cost
      heapq.heappush(queue,(cost,i[0]))

for i in range(1,V+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])

  ```
## ❗️결과
성공
## 💡접근
모든 간선의 가중치가 10이하의 자연수로 가중치가 음수인 경우는 없다.
따라서 다익스트라 알고리즘을 통해서 최단경로를 구할 수 있다. 다익스트라 알고리즘의 순서는 다음과 같다.
1. 주어진 노드사이 간선과 가중치를 저장한다.
2. 시작점을 제외한 모든 노드의 거리를 무한으로 초기화 한다. (최단거리 저장 목적)
3. 아직 방문하지 않은 노드들 중에 시작점으로 부터 거리가 가장 가까운 정점을 방문한다.
4. 방문한 노드에서 인접한 노드들에 대한 거리를 갱신해준다.

위 과정은 모든 노드를 방문하기 때문에 우선순위 큐를 이용하여 시간복잡도를 줄이는게 중요하다.

## 🧐문제 회고
대표적인 다익스트라 알고리즘을 활용한 최단거리문제였다.

# 11657 : 타임머신
## 😎solved code
### 💻code
```python
import sys

INF = int(1e9)
n,m =  map(int,sys.stdin.readline().rstrip().split())
node = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
flag = False

def bellmanFord(start):
  global flag
  distance[start] = 0
  for k in range(n+1):
    for i in range(n+1):
      for j in range(len(node[i])):
        next = node[i][j][0]
        nextCost = node[i][j][1]
        if((distance[i] != INF) and (distance[next] > distance[i] + nextCost)):
          distance[next] = distance[i] + nextCost

          #음수사이클
          if(k == n):
            flag = True
            break

for i in range(m):
  a,b,c = map(int,sys.stdin.readline().rstrip().split())
  node[a].append((b,c))

bellmanFord(1)

if(flag == False):
  for i in range(2,n+1):
    if distance[i] == INF:
      print(-1)
    else:
      print(distance[i])
else:
  print(-1)
  ```
## ❗️결과
성공
## 💡접근
A노드에서 B노드까지의 가중치가 C인 그래프로 문제를 치환한다.
이때, 위의 문제와 다르게 가중치에 음수가 있기 때문에 다익스트라 알고리즘은 사용할 수 없다.
음수 가중치가 있을 때도 최단거리를 구할 수 있는 벨만포드 알고리즘을 이용하여 문제를 해결하고자 하였다.

음수 가중치가 있을 때, 무한하게 노드사이 거리가 음수로 줄어드는 음수 사이클이 발생할 수 있다.
이때 이 음수 사이클은 N개의 노드에 대해서 거리가 INF가 아닌 노드들에 대해 (N-1)번 탐색을 진행하면 모든 노드사이의 거리를 구할 수 있다.
이를 이용하여 N번이상 탐색이 진행된다면 음수사이클이 발생하였다고 판단한다.

## 🧐문제 회고
최단거리 경로문제는 알고리즘을 확실하게 알고 있다면 어렵지않게 풀 수 있다는 생각이 든다.
BFS,DFS와 같이 공식처럼 알고리즘을 외우고, 잊지않도록 자주 들여다 봐야겠다.

# 12978 : 배달
## 😎solved code
### 💻code
```python
import sys
import heapq

def solution(N, road, K):
    INF = int(1e9)
    sorted_road = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)

    answer = 0
    queue = []
    for a,b,c in road:
        #양방향
        sorted_road[a].append((b,c))
        sorted_road[b].append((a,c))
    
    heapq.heappush(queue,(0,1))
    distance[1] = 0

	#다익스트라
    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in sorted_road[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost, i[0]))
	
    for i in range(1,N+1):
        if distance[i] <= K:
            answer += 1
			
    return answer
  ```
## ❗️결과
성공
## 💡접근
각 노드 사이 양의 가중치만 존재하는 1번 문제와 동일한 유형의 문제였다.

1. 주어진 도로의 정보 road를 다익스트라 알고리즘 탐색에 맞게 재정렬한다. 이때, 주어진 도로가 양방향임에 유의하여야 한다.
2. 시작 점이 1번마을로 정해져있기 때문에 heapq에 시작점 1번마을에서 출발하도록 초기화해준다.
3. 다익스트라 알고리즘을 통해 1번마을로부터 각 마을사이의 거리를 구한다.
4. 1번 마을과의 거리가 K 이하인 마을의 개수를 answer에 저장하여 return한다.

## 🧐문제 회고
다익스트라 알고리즘 탐색을 위한 그래프를 만들 때, 문제에 주어진 간선이 양방향인지, 단방향인지 파악 후에 실수 하지말자!