'''
기본 부품을 사용해서 중간 부품을 만든다
입력은 첫째 줄에 N이 주어지는데 1~N-1까지는 기본 부품이나 중간 부품의 번호 N은 완제품 번호
다음 줄에는 자연수 M이 주어짐 그 다음 M개의 줄에는 X,Y,K가 주어짐
x를 만드는데 Y가 K 필요하다를 나타냄
'''
import sys
from collections import deque

input = sys.stdin.readline
n = int(input()) # 노드의 개수
m = int(input()) # 간선의 개수

indegree = [0] * (n+1) # 모든 노드에 대한 전입차수를 0으로 초기화
graph = [[] for _ in range(n+1)] # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
cost = [[0] * (n + 1) for _ in range(n + 1)] # 각 부품에 필요한 기본 부품의 수

for _ in range(m): # 간선의 정보를 입력받을 반복문
    x,y,k = map(int,input().split())
    graph[y].append((x,k)) # y를 만들기 위해서는 x가 k개 필요하다
    indegree[x] += 1

def topology_sort(): #위상 정렬 함수
    result = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i) # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
            cost[i][i] = 1

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            x, k = i[0], i[1]
            indegree[x] -= 1 # 연결된 노드들의 진입차수에서 1 빼기
            if indegree[x] == 0:
                q.append(x) # 진입차수가 0이되면 삽입
            for j in range(1,n+1):
                cost[x][j] += cost[now][j] * k

topology_sort()
for i in range(1, n + 1):
    if cost[n][i]:
        print(i, cost[n][i])
        
    