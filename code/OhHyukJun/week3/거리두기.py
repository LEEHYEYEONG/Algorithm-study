def dfs(place,x,y,visited,distance):
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    
    visited[x][y] = True
    
    if distance > 0 and place[x][y] == 'P':
        return False #거리 2 이내에 P가 존재한다면 규칙 위반
    
    if distance == 2:
        return True
    
    for dx,dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 5 and 0 <= ny < 5: #5로 제한
            if visited[nx][ny] == False: #방문하지 않았고
                if place[nx][ny] != 'X': #파티션도 아니고
                    if dfs(place,nx,ny,visited,distance+1) == False: #탐색 결과 규칙위반이면 탐색 거리를 늘리고
                        return False
        
    visited[x][y] = False
    return True

def solution(places):
    answer = []
    for place in places:
        value = 1#처음에는 규칙 준수라고 가정
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    visited = [[False] * 5 for _ in range(5)]
                    if dfs(place,i,j,visited,0) == False: #place 배열과 좌표 방문 여부 거리가 들어가는 dfs 함수
                        value = 0
                        break
            if value == 0:
                break #규칙을 준수하지 않았다면
        answer.append(value)
    return answer