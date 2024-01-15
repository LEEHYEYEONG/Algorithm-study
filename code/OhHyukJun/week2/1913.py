N = int(input())
G = int(input())
Num = N**2
Num_dict = {}
array = [[0]*N for _ in range(N)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = 1, 1
i = 0
k=0
for _ in range(Num):
    Num_dict[x,y] = Num
    Num -= 1 #25,24,23,21,....,2,1
    dx,dy = directions[i]
    nx,ny = x + dx, y + dy
    if not(1<= nx <= N and 1 <= ny <= N) or (nx,ny) in Num_dict: #directions의 범위를 벗어나지 않도록 조건 설정
        i = (i+1) % 4
        dx,dy = directions[i]
    x,y = x + dx, y + dy

for i in range(N):
    for j in range(N):
        array[i][j] =(Num_dict.get((i+1,j+1)))
        print(array[i][j],end=' ')
        if j==N-1:
            print()
print([k for k, v in Num_dict.items() if v == G][0][0],[k for k, v in Num_dict.items() if v == G][0][1])