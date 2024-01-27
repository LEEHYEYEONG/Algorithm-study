import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int,sys.stdin.readline().rstrip().split()))

num_set = set(num)
num_set = list(num_set)
num_set.sort()

dic = {}
for i in range(len(num_set)):
  dic[num_set[i]] = i

for i in num:
  print(dic[i], end=" ")