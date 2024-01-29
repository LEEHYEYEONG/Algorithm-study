import sys

n = int(sys.stdin.readline().rstrip())

people = []

for i in range(n):
  age,name = sys.stdin.readline().rstrip().split()
  people.append([int(age),name,i])

#나이순, 나이가 같으면 입장순(i)으로 정렬  
people.sort(key= lambda x : (x[0],x[2]))

for age, name, ticket in people:
  print(age, name)