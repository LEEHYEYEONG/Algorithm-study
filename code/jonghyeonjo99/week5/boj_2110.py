import sys


n,c = map(int,sys.stdin.readline().rstrip().split())
houses = []
for i in range(n):
  house = int(sys.stdin.readline().rstrip())
  houses.append(house)

houses.sort()

