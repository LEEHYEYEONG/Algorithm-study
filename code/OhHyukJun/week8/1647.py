import sys
input = sys.stdin.readline

# 부모 노드를 찾는 함수
def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    return parent[x]  # 루트 노드 반환

# 두 노드를 연결하는 함수
def union(parent, a, b):
    rootA = find(parent, a)  # a의 루트 노드
    rootB = find(parent, b)  # b의 루트 노드
    
    if rootA < rootB:  # 더 작은 값이 부모 노드가 되도록 설정
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
        
N,M = map(int,input().split())
parent = [0] * (N+1)

edges = []  # 모든 간선 정보를 저장할 리스트
result = 0  # 최종 비용을 저장할 변수

# 각 노드가 자기 자신을 부모로 가지도록 초기화
for i in range(1, N+1):
    parent[i] = i
    
# 간선 정보 입력받기
for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))  # (비용, 노드a, 노드b)의 형태로 저장
    
edges.sort()  # 비용이 낮은 순으로 정렬

large = 0  # 가장 큰 비용을 저장할 변수

# 모든 간선에 대해 확인
for edge in edges:
    c,a,b = edge
    if find(parent,a) != find(parent,b):  # 두 노드가 아직 연결되지 않았다면
        union(parent,a,b)  # 두 노드를 연결
        result += c  # 비용을 합산
        large = c  # 가장 큰 비용 갱신
        
# 최종 비용에서 가장 큰 비용을 뺀 값 출력
print(result - large)
