from collections import deque

def BFS(gragh):
	seats = [] # P좌표 모음
	for i in range(5):
		for j in range(5):
			if gragh[i][j] == 'P':
				seats.append([i,j])

	for x, y in seats:
		visited = [[0 for _ in range(5)] for _ in range(5)]
		distance = [[0 for _ in range(5)] for _ in range(5)]
		visited[x][y] = True
		queue = deque()
		queue.append([x,y])
		
		while queue:
			x_now, y_now = queue.popleft()
	
			#상 우 하 좌
			dx = [-1, 0, 1, 0]
			dy = [0, 1, 0, -1]

			for i in range(4):
				nx = x_now + dx[i]
				ny = y_now + dy[i]

				if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == 0:
                    
					if gragh[nx][ny] == 'O':
						queue.append([nx, ny])
						visited[nx][ny] = 1
						distance[nx][ny] = distance[x_now][y_now] + 1
                    
					elif gragh[nx][ny] == 'P' and distance[x_now][y_now] <= 1:
						return 0

	return 1

def solution(places):
	answer = []

	for i in places:
		answer.append(BFS(i))

	return answer