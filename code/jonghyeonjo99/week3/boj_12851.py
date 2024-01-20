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