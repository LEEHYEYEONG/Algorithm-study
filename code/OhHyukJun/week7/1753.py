import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = [] #우선순위 큐 사용
    heapq.heappush(q,(0,start)) #시작 노드와 그 노드까지의 거리(0)을 push
    answer[start] = 0 #시작 노드까지의 거리를 0으로 초기화
    while q:
        dist, now = heapq.heappop(q) #가장 거리가 짧은 노드와 거리를 pop
        if answer[now] < dist:
            continue #현재 노드까지의 거리가 dist보다 작으면 continue
        for i in graph[now]: 
            cost = dist + i[1] #현재 노드를 거쳐서 가는 거리
            if answer[i[0]] > cost: #현재 노드를 거쳐 가는 거리와 기존의 거리를 비교
                answer[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
            
V,E = map(int,input().split())
K = int(input())
start = K
graph = [[] for _ in range(V+1)]
answer = [INF] * (V+1)

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

dijkstra(start)

for i in range(1,V+1):
    if answer[i] == INF:
        print("INF")
    else:
        print(answer[i])