# 1449 : 수리공 항승
## 😎solved code
### 💻code
```python
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

  ```
## ❗️결과
성공
## 💡접근
1. 인접한 물 새는 곳 사이의 거리가 주어진 테이프의 길이보다 짧다면, 하나의 테이프를 사용해서 막아주고 두 스팟 사이의 거리만큼 테이프의 길이를 잘라준다.

2. 인접한 물 새는 곳 사이의 거리가 주어진 테이프의 길이보다 길다면, 테이프를 하나 추가하여 막아준다.
## 🧐문제 회고
처음에 단순히 인접한 두 물 새는 곳 사이의 거리만 비교하여 테이프의 길이가 무한히 늘어나게 되는 실수가 있었지만, 문제에서 주어진 조건에 만족하게 구현하여 어렵지 않게 풀 수 있었다.

# 11000 : 강의실 배정
## 🥺unsolved code
### 💻code
```python
import sys
import heapq
from collections import deque

n = int(sys.stdin.readline().rstrip())
classes = []
ends = []

for i in range(n):
  lecture = list(map(int,sys.stdin.readline().rstrip().split()))
  classes.append(lecture)

classes.sort(key= lambda x : (x[0],x[1]))

start = classes[0][0]
end = classes[0][1]

ends.append(end)

classes = deque(classes)

classes.popleft()

for s, t in classes:
  for i in range(len(ends)):
    if(s < ends[i]):
      ends.append(t)
      ends.sort()
      break
    else: #(s >= ends[i])
      ends[i] = t
      ends.sort()
      break

print(len(ends))

  ```
## ❗️결과
시간초과
## 💡접근
1. 강의 시작이 빠른 순서로, 시작 시간이 같다면 끝나는 시간이 빠른 순으로 정렬한다.
2. 다음 강의 시작시간이 그 전 강의 종료시간보다 빠르다면, 새로운 강의실을 구한다.
3. 다음 강의 시작시간이 그 전 강의 종료시간보다 늦거나 같다면, 기존 강의실을 사용한다.

위의 접근을 토대로 이중 for문을 이용해 구현하였다. 하지만 강의 개수 N의 범위가 200,000 인 것을 나중에 확인하고, 위 코드의 시간복잡도가 O(n^2)이 되어 시간초과가 발생하였다.

  ## 😎solved code
  ### 💻code
```python
import sys
import heapq
from collections import deque

n = int(sys.stdin.readline().rstrip())
classes = []
ends = []

for i in range(n):
  lecture = list(map(int,sys.stdin.readline().rstrip().split()))
  classes.append(lecture)

classes.sort(key= lambda x : (x[0],x[1]))

end = classes[0][1]

classes = deque(classes)
classes.popleft()

heapq.heappush(ends,end)

for i in range(len(classes)):
  if(ends[0] > classes[i][0]):
    heapq.heappush(ends, classes[i][1])
  else:
    heapq.heappop(ends)
    heapq.heappush(ends, classes[i][1])

print(len(ends))

  ```
## ❗️결과
성공
## 💡접근
위와 같은 접근을 사용하지만 시간초과를 피하기 위해 heapq 자료구조를 사용하였다.
heapq는 파이썬에서 우선순위 큐를 사용할 때 자주 쓰이는 모듈로, 따로 sort해주지 않아도 알아서 원소들을 최소힙으로 정렬해준다.

이를 활용해서 강의실의 최소 개수를 구하였다.
## 🧐문제 회고
항상 문제를 풀기 전에 주어진 변수들의 범위를 확인하고, 시간초과 여부를 체크하는 것을 잊지말자!

# 72411 : 메뉴 리뉴얼
## 🥺unsolved code
### 💻code
```python
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

  ```
## ❗️결과
실패
## 💡접근
1. 결과값이 알파벳 순서이고 조합의 중복을 피하기 위해 ((예시)'AB' 와 'BA) 가장 먼저 알파벳 순으로 정렬해주었다.
2. 그 후 주어진 orders를 course의 가짓수에 맞게 주어진 모든 조합의 경우의 수를 구했다.(combinations 모듈 사용)
3. 구한 조합들 중 중복되는 조합을 list에 저장하고 그 갯수를 센다.(Counter 모듈 사용)
4. 갯수가 많은 코스 요리를 return 한다. 

## 🧐문제 회고
위의 접근을 토대로 문제를 풀었지만, Counter에 순서가 없어 원하는 값을 추출하는 로직을 생각하지 못했다.
또, 문제를 풀면서 모듈을 2개 사용했고 3중 for문도 있어 변수의 범위가 작긴하지만
시간초과의 가능성도 높아보인다.
