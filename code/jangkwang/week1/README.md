### 코딩테스트는 파이썬으로 작성하였습니다.

# 1. 백준 1449 SILVER3

## 1-1. 어떤 문제인가?

그리디 알고리즘에 맞게 for문을 돌며 풀어보자 1. 물 새는 곳을 막아라! 2. 근데 테이프 길이에 맞게 3. 테이프 길이에 맞게 막았으면 테이프 붙이기를 이어나간다! 4. 못 막았으면 카운트를 추가하며 새로운 테이프를 붙인다.

## 1-2. 문제 해설

```python
N, L = map(int, input().split())
# N = 물 새는 곳의 갯수
# L = 테이프 길이
T = list(map(int, input().split())) // T에 N만큼의 숫자를 입력받고
T.sort() // 제일 가까운 구멍부터 찾기위해 오름차순으로 정렬한다!
cnt = 1 // 테이프는 무조건 하나 이상을 붙일 것이기에 1로 초기화한다.

# print(T)
for i in T[1:]: // 만약 T의 2번째 수가
    if i in range(T[0], T[0] + L): // L(길이)만큼 더한 길이 안에 i(T값)이 존재한다면
        continue // 넘어가고
    else: // 테이프를 붙일 수 없는 길이라면
        T[0] = i // 첫 번쨰 순서를 바꾼후
        cnt += 1 // 카운트를 세준다~

print(cnt) // 최종적으로 붙인 테이프의 갯수를 return 한다.
```

# 2. 백준 11000 GOLD5

## 2-1. 그대들은 어떻게 풀 것인가

- 솔직히 heapq에 대한 것을 처음 알았다. 구글링 후 알았다.
- 타 풀이를 참고하여 heapq를 사용하여 풀었다.
- heapq는 배열의 맨 처음은 push한 가장 작은 값이 먼저 들어간다.
- pop도 마찬가지로 배열안 가장 작은 값이 지워진다. 이 원리를 이용해 풀어보자.

## 2-2. 문풀

```python
from heapq import heappush, heappop // hepq의 push, pop을 불러온다.
# S에 시작해서 T에 끝나는 수업 N개
# 최소의 강의실 => 모든 수업을 들어야 함
# 수업이 끝나야 다음 수업 가능
N = int(input()) // N만큼 정수 값을 입력받고

input_arr = [] // input_arr라는 입력값을 받을 빈 배열을 선언해준다.

for i in range(N):
    start, end = map(int,input().split()) # 입력 받고
    input_arr.append([start,end]) # 저장

input_arr.sort() // 오름차순으로 정렬해줌
result=[] // 최종 리턴할 result를 빈 배열로 초기화해준다.
heappush(result, input_arr[0][1]) #heapq는 가장 원소 값이작은 것을 처음으로 빼기 때문에 필요함
// result에 가장 시작이 빠른 수업의 끝나는 시간을 저장해준다.
# 즉 첫 수업 시작을 제일 빠른 시간표로 하기 위해서!
# print(input_arr, result)

# 만약 result >= input_arr[i][0] 이면 패스하고 다음 순서로
# 다음순서가 <=이면 끝낸다.
# 그 다음 arr[i+1][0]로 넘어가서

for i in range(1,N):
    if result[0] > input_arr[i][0]: # 같이 들을 수 없는 경우
        // 같이 들을 수 없는 경우에
        heappush(result, input_arr[i][1]) # 같이 들을 수 없는 수업의 끝나는 시간을 result에 담는다.
        // 끝나는 시간을 담아주고
    else: # 같이 들을 수 있는 경우
        heappop(result) # 같이 들을 수 있다면 가장 값이 적은(수업이 가장 빨리 끝나는)값을 없애준다.
        // 같이 들을 수 있다면 가장 빨리 시작한 수업을 result에서 지워준다.
        heappush(result, input_arr[i][1]) // 그리고 마찬가지로 담아준다.

print(len(result)) // 최종적으로 남은 result배열안의 갯수를 return 해준다.



```

# 3. 프로그래머스

## 3-1. 추후 풀이 예정 ㅠㅠㅠ 죄송합니다.
