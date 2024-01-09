# 중앙을 시작으로 상우하좌(달팽이 모양) 이동하면서 숫자를 채워넣는 방식 

n = int(input())
m = int(input())

# 방향
# 우, 하, 좌, 상
dx = [0, 1, 0, -1]  
dy = [1, 0, -1, 0]

# N^2으로 이루어진 배열 
n_list = [[0 for _ in range(n)] for _ in range(n)]

# 시작 지점
num = 1
x, y = n//2, n//2
n_list[x][y] = num

# 특정 방향으로 얼마나 이동할 지 
len = 0
if m == 1:
    ans = [x+1, y+1]

while True:
    for i in range(4):
        for _ in range(len):
            x += dx[i]
            y += dy[i]
            num += 1
            n_list[x][y] = num
            if num == m:
                ans = [x+1, y+1]
    
    if x==y==0:
        break
    x -= 1
    y -= 1
    len += 2

for i in range(n):
    print(*n_list[i])
print(*ans) 
