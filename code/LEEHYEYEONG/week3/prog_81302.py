def check(place):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                for w in range(4):
                    nx, ny = i+dx[w], j+dy[w]
                    if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] == 'P':
                        return 0
            elif place[i][j] == 'O':
                count = 0
                for w in range(4):
                    nx, ny = i+dx[w], j+dy[w]
                    if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] == 'P':
                        count += 1
                
                if count >= 2:
                    return 0                  
    return 1

def solution(places):
    answer = []
    for i in range(5):
        answer.append(check(places[i]))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))


