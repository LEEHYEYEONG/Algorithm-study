import sys

input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
n, m = map(int, input().split())

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
parent = [i for i in range(n + 1)]

edges = []
result = 0

# 간선을 입력받아 cost를 기준으로 오름차순 정렬
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

edges.sort(key=lambda x: x[2])

max_cost = 0

# 정렬된 간선을 하나씩 확인
for edge in edges:
    a, b, cost = edge
    # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은것이므로  
    if find_parent(parent, a) != find_parent(parent, b):
        # 신장 트리에 간선 추가
        union_parent(parent, a, b)
        result += cost
        max_cost = cost

print(result - max_cost)