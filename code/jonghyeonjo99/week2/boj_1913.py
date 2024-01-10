import sys


n = int(sys.stdin.readline().rstrip())
q = int(sys.stdin.readline().rstrip())

board = [[0 for _ in range(n)] for _ in range(n) ]
x = 0
y = 0
result_x = n//2 + 1
result_y = n//2 + 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

board[x][y] = n ** 2
num = n ** 2 - 1

for k in range(n//2):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    while(True):
      if(nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] != 0 ):
        break
      board[nx][ny] = num
      if(num == q):
        result_x = nx+1
        result_y = ny+1
      num -= 1
      x = nx
      y = ny
      nx = x + dx[i]
      ny = y + dy[i]

board[n//2][n//2] = 1
if(q == n**2):
  result_x = 1
  result_y = 1

for i in board:
  print(*i)

print(result_x, result_y)