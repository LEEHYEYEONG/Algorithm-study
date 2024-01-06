# 백준 1449번

## 접근

1. 구멍이 난 곳에서 양 옆으로 간격이 0.5가 나야하므로 구멍이 난 위치에서 테이프의 길이를 더하고 0.5를 빼는 방식으로 현재 테이프의 끝이 어디에 있는지 저장
   <br>

```python
pointer = location[0] + l - 0.5
```

2. 만약 이 포인터와 다음 구멍이 난 위치에서 0.5를 더한 것과 비교하여 pointer가 크거나 같으면 커버가 가능한 위치에 있으므로 continue

```python
    if(pointer >= location[i] + 0.5):
        continue
```

3. 비교하여 pointer보다 더 크다면 pointer 값을 갱신하고 tape를 1증가

```python
    pointer = location[i] + l - 0.5
    tape += 1
```

<br>

# 백준 11000번

## 접근

강의 시작시간과 종료시간을 담은 리스트를 room_list에 저장

```python
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    room_list.append([a, b])
```

`sort()`를 사용해서 room_list를 정렬 `a`를 기준으로 정렬

```python
room_list.sort()
```

이전 강의의 종료시간과 다음 강의의 시작 시간을 비교해서 종료시간이 되었다면 pop하고 아니라면 push 해준다.
<br>
하지만 여기의 문제점은 가장 빨리 끝나는 강의 시간을 알기 위해서는 계속 정렬이 필요한데 sort로 계속 정렬하기엔 시간초과 발생

```python
for i in range(1, n):
    if room[0] <= room_list[i][0]:
        room.pop(0)

    room.append(room_list[i][1])
    room.sort()
```

그래서 문제를 해결하지 못하고 있었는데 `heapq`라이브러리를 알게 됨
<br>
heapq는 가장 작은 요소가 가장 앞에 위치하도록 자동으로 정렬됨
-> sort를 사용한 시간초과 해결

```python
for i in range(1, n):
    if room[0] <= room_list[i][0]:
        heapq.heappop(room) # 가장 작은 항목 반환
    heapq.heappush(room, room_list[i][1])
```

<br>

# 프로그래머스 메뉴 리뉴얼

## 접근

`itertools` 라이브러리를 알고 있어서 combinations으로 course에 있는 개수만큼 뽑기로 했음
`from itertools import combinations`
<br>
뽑은 후에 문자열로 다시 조합한 후 `combi_list`에 추가

`Counter의 most_common`
<br> 세는 방법을 직접 구현하려다가 Counter이라는 라이브러리를 찾았고 most_common이라는 함수를 사용
<br>

### most_common

n개의 가장 흔한 요소와 그 개수를 가장 흔한 것부터 가장 적은 것 순으로 나열한 리스트를 반환. n이 생략되거나 None이면 모든 요소를 반환.
<br>
가장 많이 나온것부터 나열한 리스트를 반환하기 때문에 여기에서 max_count를 간편하게 구할 수 있음

```python
    for i in course:
        combi_list = list()
        for j in orders:
            combi = list(map(lambda x: ''.join(x), combinations(j, i)))
            combi_list.extend(combi)
            menu[i] = Counter(combi_list).most_common()
```

```python
max_count = menu[i][0][-1]
```

<br>
그 후 저장된 menu 딕셔너리에서 1이 아닌 max_count와 같다면 정답 배열에 저장하고 정렬된 배열을 반환한다.

## 문제

테스트케이스 3의 경우 초기에 orders를 문자별로 정렬해놓지 않으면 XW와 WX를 다르게 보고 개수를 셈

```python
orders = list(map(sorted, orders))
```

이 부분을 추가

Counter를 사용하는 법을 잘 몰랐는데 이 문제를 통해서 사용법을 익히게 되었다.
