import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def solution(N, road, K):
    answer = 0
    distance = [INF]*(N+1)
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    #while 문 구현 실패

    for d in distance[1:]:
        if d <= K:
            answer += 1
    return answer