import sys

n = int(sys.stdin.readline().rstrip())
budget_list = list(map(int,sys.stdin.readline().rstrip().split()))
total_budget = int(sys.stdin.readline().rstrip())

left = 0
right = max(budget_list)
mid = 0
result = 0

while(left <= right):

  mid = (left+right) // 2
  count = 0

  for budget in budget_list:
    if(budget >= mid):
      count += mid
    else:
      count += budget
  
  if(count > total_budget):
    right = mid -1

  elif(count <= total_budget):
    if(mid > result):
      result = mid

    left = mid + 1

print(result)