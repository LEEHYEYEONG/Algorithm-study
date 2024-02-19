import sys
import heapq

def solution(N, road, K):
    INF = int(1e9)
    sorted_road = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)

    answer = 0
    queue = []
    for a,b,c in road:
        #양방향
        sorted_road[a].append((b,c))
        sorted_road[b].append((a,c))
    
    heapq.heappush(queue,(0,1))
    distance[1] = 0

	#다익스트라
    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in sorted_road[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost, i[0]))
	
    for i in range(1,N+1):
        if distance[i] <= K:
            answer += 1
			
    return answer