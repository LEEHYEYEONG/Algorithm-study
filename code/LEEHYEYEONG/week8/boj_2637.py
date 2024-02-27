from collections import deque

n = int(input())
m = int(input())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

# 필요한 부품을 저장하는 리스트
needs = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append([x, k]) # x를 만드는데 y가 k개 필요 
    indegree[x] += 1 # 진입차수 

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            result.append(i) # 기본부품 리스트 
            q.append(i)
    
    while q:
        now = q.popleft()
        for object, k in graph[now]:
            if now in result: # 기본부품일 경우 목적제품에 +n개 
                needs[object][now] += k
            else:
                for i in range(1, n+1):
                    needs[object][i] += needs[now][i]*k
            indegree[object] -= 1
            if indegree[object] == 0:
                q.append(object)
    
    for i in range(n+1):
        if needs[n][i] > 0:
            print(i, needs[n][i])

topology_sort()