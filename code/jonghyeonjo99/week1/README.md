# 1449 : 수리공 항승
### code
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
## 결과
성공
## 접근
1. 인접한 물 새는 곳 사이의 거리가 주어진 테이프의 길이보다 짧다면, 하나의 테이프를 사용해서 막아주고 두 스팟 사이의 거리만큼 테이프의 길이를 잘라준다.

2. 인접한 물 새는 곳 사이의 거리가 주어진 테이프의 길이보다 길다면, 테이프를 하나 추가하여 막아준다.
## 문제 회고
처음에 단순히 인접한 두 물 새는 곳 사이의 거리만 비교하여 테이프의 길이가 무한히 늘어나게 되는 실수가 있었지만, 문제에서 주어진 조건에 만족하게 구현하여 어렵지 않게 풀 수 있었다.

# 1234 : ABCD
### code
```python

  ```
## 결과

## 접근

## 문제 회고

# 1234 : ABCD
### code
```python

  ```
## 결과

## 접근

## 문제 회고
