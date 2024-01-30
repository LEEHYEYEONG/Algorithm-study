N = int(input())
G = int(input())

def solution(N,G):
    Num = N**2
    Num_dict = {}
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    x,y = 1,1
    i = 0
    for _ in range(Num):
        Num_dict[x,y] = Num
        Num -= 1
        dx,dy = directions[i]
        nx,ny = x+dx,y+dy
        if not(1 <= nx <= N and 1 <= ny <= N) or (nx,ny) in Num_dict:
            i = (i+1)%4 #배열의 길이를 넘지 않도록
            dx,dy = directions[i]
        x,y = x+dx, y+dy
    array = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            array[i][j] = Num_dict.get((i+1,j+1))

    position = [k for k,v in Num_dict.items() if v == G][0]
    return array,position


matrix, position = solution(N,G)
for i in matrix:
    print(' '.join(map(str,i)))
print(position[0],position[1])