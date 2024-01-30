import sys


n, l = map(int,sys.stdin.readline().rstrip().split())
spots = list(map(int,sys.stdin.readline().rstrip().split()))
count = 1

spots.sort()

tape = l
for i in range(1,len(spots)):
  spot_distance = spots[i] - spots[i-1]
  if(spot_distance < tape):
    tape -= spot_distance
  elif(spot_distance >= tape):
    count += 1
    tape = l

print(count)
