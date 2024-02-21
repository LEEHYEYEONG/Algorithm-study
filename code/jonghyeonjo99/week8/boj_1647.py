import sys
import heapq

n,m = map(int,sys.stdin.readline().rstrip().split())
billiage = []
queue = []
size = 0
parent = [0] * (n+1)

def find(k):
  if parent[k] != k:
    return find(parent[k])
  return k

def union(a,b):
  a = find(a)
  b = find(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for i in range(1,n+1):
  parent[i] = i

for i in range(m):
  a,b,c = map(int,sys.stdin.readline().rstrip().split())
  billiage.append((c,a,b))

billiage.sort()

for i in range(m):
  if(find(billiage[i][1]) != find(billiage[i][2])):
    union(billiage[i][1], billiage[i][2])
    heapq.heappush(queue,(-billiage[i][0],billiage[i][0]))
    size += billiage[i][0]

max_road = heapq.heappop(queue)[1]

print(size - max_road)