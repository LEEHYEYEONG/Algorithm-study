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
