from collections import deque

Max = 10 ** 5
N,K = map(int,input().split())
visited = [0] * (Max+1) #위치에 도달하는 데 걸리는 시간을 저장하는 배열 인덱스는 위치 값은 방문 여부

def bfs():
    queue = deque([(N,0)]) #위치값과 시간값을 저장
    visited[N] = 1 #수빈이의 위치를 처음 방문 값으로 설정
    count = 0 #최단 시간 경우의 수를 출력할 때 사용할 변수
    min_time = None #최단 시간을 저장할 비어있는 변수
    
    while queue:
        X, time = queue.popleft()
        
        if min_time != None and time > min_time:
            continue #시간복잡도를 줄이기 위해 추가한 코드
        
        if X == K:
            if min_time == None: #처음 구해진 N==K 값일 때
                min_time = time
            count += 1
        
        for i in (X-1, X+1, 2*X):
            if 0 <= i <= Max:
                if not visited[i] or (visited[i] and time+1 <= visited[i]):
                    visited[i] = time+1
                    queue.append((i,time+1))
                    
    print(min_time)
    print(count)
bfs()