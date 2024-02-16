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
## 🥺unsolved code
### 💻code
```python

  ```
## ❗️결과

## 💡접근

## 🧐문제 회고

# 12978 : 배달
## 😎solved code
## 🥺unsolved code
### 💻code
```python

  ```
## ❗️결과

## 💡접근

## 🧐문제 회고