def check(place):
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, -1, 1]

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                for w in range(8):
                    nx, ny = i + dx[w], j + dy[w]
                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                        continue
                    if place[nx][ny] == 'P':
                        if w < 4:
                            return 0
                        elif place[i + (dx[w] // 2)][j + (dy[w] // 2)] != 'X':
                            return 0
    return 1

def solution(places):
    answer = []
    for i in range(5):
        answer.append(check(places[i]))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))


