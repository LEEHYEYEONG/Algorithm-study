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