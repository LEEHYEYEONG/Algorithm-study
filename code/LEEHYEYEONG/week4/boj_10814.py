import sys

n = int(sys.stdin.readline())

member = []

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    member.append([int(age), i, name])

member.sort(key= lambda x:(x[0], x[1]))

for i in range(n):
    print(member[i][0], member[i][2])