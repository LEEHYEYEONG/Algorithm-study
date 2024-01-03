## 1. 그리디

### 수리공 항승 (1449) 
<aside>
💡 문제 정리

1. 파이프에서 물이 새는 곳 - 가장 왼쪽에서 정수만큼 떨어진 거리의 장소
2. 길이가 L인 테이프로 물이 새는 곳을 막음 
    - 적어도 좌우 0.5만큼 간격을 두고 테이프를 붙여야함
3.  물이 새는 곳 위치와 테이프 길이 L이 주어졌을 때, 필요한 테이프의 최소 개수 테이프를 자르거나 겹쳐서 붙이는 것 불가

입력

- 첫째 줄에 물이 새는 곳의 개수 N과 테이프 길이 L 둘째 줄에는 물이 새는 곳의 위치
- 0 < N, L, 물이 새는 위치 <= 1000
</aside>

문제 접근
1. 물이 새는 위치 오름차순 정렬(sort)
2. 시작점, 테이프 숫자를 변수로 선언
3. 반복문을 물이 새는 위치 안에서 돌리면서 위치 사이의 간격이 L보다 큰가 아닌가를 판단


### 강의실 배정 (11000)
<aside>
💡 문제 정리

1. Si에 시작해서 Ti에 끝나는 N개의 수업
2. 이때 최소의 강의실 구하기
3. 수업이 끝나야 다음 수업 가능

입력

- 첫 번째 줄: N(1 ≤ N ≤ 200,000)
- N개의 줄에 Si, Ti(0 ≤ Si < Ti ≤ 109)
</aside>

문제 접근
1. si를 기준으로 값을 정렬
2. 다음 강의의 시작 시간과 종료 시간을 이전 강의와 비교하며 값 추가
3. 우선 순위 큐 사용해야 할듯(실패 코드 이후에 추가한 내용..)

### 실패 코드
1. 틀림
```python
N=int(input()) 
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x:x[0])
count = 1
for i in range(N):
    if arr[i][0] <= arr[i+1][0] and arr[i+1][0] < arr[i][1]:
        count+=1
    else:
        continue
print(count)
```

2. 시간 초과(이중 for문 때문인듯) 
```python
N=int(input()) 
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x:x[0])
count = 0
end_times = []
for i in range(N):
    for j in range(count):
        if end_times[j] <= arr[i][0]:
            end_times[j] = arr[i][1]
            break
    else:
        end_times.append(arr[i][1])
        count+=1
print(count)
```

3. 역시나 시간 초과(그래도 이중 for 문 사용 시보다는 줄어들었다.)
```python
import heapq

N=int(input()) 
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x:x[0])

count = [arr[0][1]]
for i in range(N):
    if count and count[0] <= arr[i][0]:
        heapq.heappop(count)
    heapq.heappush(count, arr[i][1])

print(len(count))
# 처음엔 sort 부분이 문제일까 했지만 input말고 sys.stdin.readline 사용하니 해결되었다..너무 프로그래머스만 풀었나봄
```

### 2. 실전

- 문제정보 : 메뉴 리뉴얼 (72411)
- 출처 : 프로그래머스
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/72411
