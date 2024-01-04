from itertools import combinations
from collections import Counter

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

sorted_orders = []
com_result = []
result = []

for order in orders:
  order = sorted(order)
  sorted_orders.append(order)

sorted_orders.sort()

for i in course:
  for order in sorted_orders:
    for com in combinations(order,i):
      com_result.append(com)

for i in range(len(com_result)):
  for j in range(1,len(com_result)):
    if(com_result[i] == com_result[j] and i != j):
      result.append(com_result[i])

result = list(map("".join, result))

counter = Counter(result)



print(counter)
