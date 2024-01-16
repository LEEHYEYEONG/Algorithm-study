import sys
from collections import defaultdict

# 그래프 구현 
graph = defaultdict(list)

n, m, v = map(int, input().split())

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 리스트 구현
def dfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            graph[node].sort(reverse=True)
            need_visited.extend(graph[node])
    
    return visited

# dfs 재귀 구현
def recursive_dfs(v, visited = []):
    visited.append(v) # 시작 정점 방문
    graph[v].sort()
    for w in graph[v]:
        if not w in visited: # 방문 하지 않았으면
            visited = recursive_dfs(w, visited)
    return visited

# bfs 리스트 구현
def bfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        
        if node not in visited:
            visited.append(node)
            graph[node].sort()
            need_visited.extend(graph[node])
    return visited


print(*dfs(graph, v))
#print(recursive_dfs(v))
print(*bfs(graph, v))