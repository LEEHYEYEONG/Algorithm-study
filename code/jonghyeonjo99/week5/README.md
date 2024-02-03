# 2512 : 예산
## 😎solved code
### 💻code
```python
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
  ```
## ❗️결과
성공
## 💡접근
M이 10억이하의 숫자이기 때문에 완전탐색을 하게되면 무조건 시간초과가 발생하게 된다. 따라서 이진탐색을 통해서 예산 배정을 하기로 하였다.
1. 배정받고자하는 예산안 리스트 중 가장 큰 값을 right 값으로 두고, 문제의 조건대로 예산안을 모두 더한다.
2. 합쳐진 예산안(count)가 총 예산안보다 적다면, 배정된 예산을 늘려주고 크다면, 배정된 예산안을 이분탐색에 맞게 줄여준다.
3. 총 예산안의 범위내에서 가장 많은 예산을 줄 수 있는 값을 출력한다.

## 🧐문제 회고
문제의 입력조건을 보고 무조건 이분탐색임을 확인할 수 있었다.
이분탐색의 대상이 어떤 값인지를 잘 선정하는 능력을 기르자!

# 1234 : ABCD
## 😎solved code
## 🥺unsolved code
### 💻code
```python

  ```
## ❗️결과

## 💡접근

## 🧐문제 회고

# 1234 : ABCD
## 😎solved code
## 🥺unsolved code
### 💻code
```python

  ```
## ❗️결과

## 💡접근

## 🧐문제 회고