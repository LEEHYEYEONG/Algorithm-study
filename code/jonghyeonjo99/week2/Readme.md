# 1913 : 달팽이 
## 😎solved code
### code
```python
import sys


n = int(sys.stdin.readline().rstrip())
q = int(sys.stdin.readline().rstrip())

board = [[0 for _ in range(n)] for _ in range(n) ]
x = 0
y = 0

#q가 1일 경우 좌표값
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

#달팽이 시작 좌표의 숫자값
board[n//2][n//2] = 1

#q가 N의 제곱일 경우 좌표값
if(q == n**2):
  result_x = 1
  result_y = 1

#unpacking
for i in board:
  print(*i)

print(result_x, result_y)
  ```
## ❗️결과
성공
## 접근
1. 표의 인덱스 (0,0)부터 달팽이가 지나온 반대방향으로 표를 복원해준다.
    - 표를 (상,하,좌,우) 한바퀴 도는 것을 기준으로 봤을 때, 달팽이는 n//2 번 표를 순회한다.
    - 달팽이는 n//2번 상,하,좌,우로 회전하는데 표를 벗어나거나 이미 지나간 자리는 다시 가지 않는다.
    - 표를 순회하며 숫자를 채우다가 위치를 찾고자 하는 숫자가 나타나면 좌표를 저장한다.
2.  표의 시작과 끝은 직접 초기화 시켜주기 때문에 좌표를 원하는 숫자가 1 또는 n**2 라면 예외적으로 좌표값을 설정하여준다.

## 문제 회고
while문과 for문, 조건문을 모두 사용해서 달팽이가 지나온 표를 복원하는 과정이 까다로웠다.

위치를 찾고자 하는 숫자가 1 혹은 n**2인 경우에는 직접 좌표값을 설정해주어야하는 예외사항은 비교적 빠르게 찾아 문제를 풀 수 있었다. 

# 14719 : 빗물
## 😎solved code
### 💻code
```python
import sys

h, w = map(int,sys.stdin.readline().rstrip().split())
wall = list(map(int, sys.stdin.readline().rstrip().split()))

world = [[0 for _ in range(w)] for _ in range(h)]

for i in range(w):
  hight = wall[i]
  for j in range(h-1, -1, -1):
    if(hight > 0):
      world[j][i] = 1
    hight -= 1

result = 0

for i in range(h):
  temp = 0
  flag = False
  for j in range(w-1,-1,-1):
    
    if(world[i][j] == 1):
      if(flag == True and temp > 0):
        result += temp
        temp = 0
      flag = True
    elif(flag == True):
      temp += 1

print(result)
  ```
## ❗️결과
성공
## 💡접근
1. 우선 world에 블럭을 세워 벽을 만든다.
2. world의 바닥부터 가로로 한 줄씩 순회한다.
3. 처음 벽을 만나면(1을 만나면) flag값을 True로 바꿔준다.
4. flag == True 일 때, 고일 수 있는 빗물을 temp에 더해준다.
5. 이후 다시 벽을 만나면(1을 만나면) 빗물이 고일 수 있는 양쪽 벽이 있는 것이기 때문에 temp에 더해줬던 값을 result에 더해준다.
6. 만약 두번째 벽을 만나지 못했다면 temp = 0 으로 초기화 해준다.

## 🧐문제 회고
빗물이 고이는 조건은 비교적 빠르게 생각했지만, 그 생각을 코드로 구현하는 과정이 까다로웠다. 3개 이상의 조건으로 분기해야하는 문제에서 조건의 우선순위를 생각하여 적절하게 배치하는 것이 중요하다는 것을 배울 수 있었다.

# 1234 : ABCD
## 😎solved code
## 🥺unsolved code
### 💻code
```python

  ```
## ❗️결과

## 💡접근

## 🧐문제 회고