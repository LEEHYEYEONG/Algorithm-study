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