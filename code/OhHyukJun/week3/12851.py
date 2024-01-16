from collections import deque

visited = [0] * (10**5 + 1) #최대 100,000
N,K = map(int,input().split())

def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        X = queue.popleft()
        if X == K:
            print(visited[X])
            break
        for i in (X-1, X+1, 2*X):
            if 0 <= i <= 10**5 and not visited[i]:
                visited[i] = visited[X] + 1
                queue.append(i)

bfs()
                