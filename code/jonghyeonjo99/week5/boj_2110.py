import sys


n,c = map(int,sys.stdin.readline().rstrip().split())
houses = []
for i in range(n):
  house = int(sys.stdin.readline().rstrip())
  houses.append(house)

houses.sort()

left = 0
right = houses[-1] - houses[0]
mid = 0
result = 0
while(left <= right):
  mid = (left + right) // 2
  current = houses[0]
  count = 1
  for i in range(1, len(houses)):
    if (houses[i] >= current + mid):
      count += 1
      current = houses[i]

  if(count >= c):
    left = mid + 1
    result = mid
  else:
    right = mid - 1

print(mid) 