# 백준 2512번

## 접근

이렇게 입력을 받고 만약 모든 요청이 배정될 수 있는 경우는 아래와 같이 처리했다.

```python
n = int(input())
money = list(map(int, input().split()))
max_sum = int(input())

# 모든 요청이 배정될 수 있는 경우
if(sum(money) <= max_sum):
    print(max(money))
```

모든 요청이 배정되지 않는 경우 money에서 가장 큰 수를 하나씩 줄여가면서 값을 변경해주었다.

이 경우 시간초과가 난다.

```python
def add(max_number, money):
    result = 0
    for i in money:
        if(i < max_number):
            result += i
        else:
            result += max_number

    return result

# 모든 요청이 배정될 수 있는 경우
if(sum(money) <= max_sum):
    print(max(money))
# 모든 요청이 배정되지 않는 경우
else:
    max_number = max(money)
    while (add(max_number, money) > max_sum):
        max_number -= 1
    print(max_number)
```

이진 탐색을 이용하지 않는 경우는 시간초과가 발생하는 것같다.

### 이진 탐색

- 오름차순으로 정렬된 상태여야 함
- 자료의 중간값이 찾고자하는 타겟값인지를 비교

이진 탐색을 이용하여 시간초과를 해결해보겠다.

이를 이용해 타겟값은 → 예산 (예산 값보다 작아지는 경우)

start = 1, end = max(money)

mid = (start + end)

```python
# 모든 요청이 배정되지 않는 경우
else:
    start = 1
    end = max(money)
    while start <= end:
        mid = (start + end) // 2
        if(add(mid, money) <= max_sum):
            start = mid + 1
        else:
            end = mid - 1
    print(end)
```

이 경우 1부터 max(money)까지를 고려하기 때문에 따로 정렬은 필요하지 않다.

처음에는 `start += 1, end -=1`로 구현하였는데 여전히 시간초과가 발생했다.

mid를 이용해서 값을 갱신해주어야 한다.

처음 1, max에서 중간 값을 해준 후 max_sum보다 작다면 이 값 아래는 볼필요가 없다는 뜻이기에 mid +1 을 해주어야 하고

만약 초과한다면 1, max의 중간 값에서 중간 값 위로는 볼 필요가 없기 때문에 mid - 1을 해주어야 한다.

## 참고

이진 탐색

[[알고리즘 / Python] 이분 탐색 / 이진 탐색 (Binary Search)](https://code-angie.tistory.com/3)

<br>

# 백준 2110번

## 접근

예제의 집의 좌표를 오름차순으로 정렬하면

1 2 4 8 9

3개를 설치면 1, 4, 9에 설치 그렇기에 가장 인접한 두 공유기의 거리는 3

일단 입력 받은 집의 좌표들을 오름차순으로 정렬해야 할 것 같다.

```python
n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()
```

만약 C가 4라면, 1, 2, 4, 9 이거나 1, 4, 8, 9에 설치가 될 것이다. 그러면 1이 된다.

C를 맨 처음, 맨 끝에 배정한 후 그 좌표의 중앙, 또 중앙 이런 식으로 접근해야 하지 않을까?

홀수이면 → 중간 값에 설치

짝수이면 → 양끝 값과 더 차이가 큰 곳에 설치

그리고 그 수를 기준으로 나눈 배열을 반환하도록 함수를 만들었고

```python
# 중간 인덱스의 값을 이용하여 새로운 배열을 반환
def place(arr, answer):
    if len(arr) % 2 == 0:
        index1 = len(arr) // 2 - 1
        index2 = index1 + 1

        max_number = arr[index1] if arr[index1] - arr[0] > arr[len(arr)-1] - arr[index2] else arr[index2]
        max_index = arr.index(max_number)
        answer.append(arr[max_index])
        return [arr[0:max_index+1], arr[max_index:len(arr)]]

    else:
        arr_index = (len(arr) - 1) // 2
        answer.append(arr[arr_index])
        return [arr[0:arr_index+1], arr[arr_index:len(arr)]]
```

배열의 개수만큼 반복문을 돌려

```python
while c:
    arr1 = []
    for i in arr:
        arr1.extend(place(i, answer))
        c -= 1
    arr = arr1
```

뺀 값 중에 가장 작은 값을 출력하도록 만들었는데

```python
answer.sort()

print(min([answer[i+1] - answer[i] for i in range(len(answer) - 1)]))
```

예제를 넣으면 3으로 출력되기는 하지만 다른 값들을 넣으면 제대로 작동하지 않았다.

아마 공유기 설치가 3개 정도까지만 되는 것 같다,,ㅎ

### 실패 코드

```python
n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

start, end = 0, n - 1
answer = [house[0], house[n-1]]
c -= 2

# 중간 인덱스의 값을 이용하여 새로운 배열을 반환
def place(arr, answer):
    if len(arr) % 2 == 0:
        index1 = len(arr) // 2 - 1
        index2 = index1 + 1

        max_number = arr[index1] if arr[index1] - arr[0] > arr[len(arr)-1] - arr[index2] else arr[index2]
        max_index = arr.index(max_number)
        answer.append(arr[max_index])
        return [arr[0:max_index+1], arr[max_index:len(arr)]]

    else:
        arr_index = (len(arr) - 1) // 2
        answer.append(arr[arr_index])
        return [arr[0:arr_index+1], arr[arr_index:len(arr)]]

arr = [house[start:end+1]]

while c:
    arr1 = []
    for i in arr:
        arr1.extend(place(i, answer))
        c -= 1
    arr = arr1

answer.sort()

print(min([answer[i+1] - answer[i] for i in range(len(answer) - 1)]))
```

그래서 이진 탐색을 위한 풀이를 참고했다.

공유기의 거리를 이진 탐색을 통해 찾고

설정한 공유기의 거리를 통해 공유기를 몇 대 설치할 수 있는 지 확인한다.

공유기 수가 목표보다 크면 공유기 사이의 거리를 늘리고 목표보다 작으면 공유기 사이의 거리를 줄이는 풀이이다.

```python
while (start <= end):
    # 현재 공유기 거리
    mid = (start + end) // 2
    current = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= current + mid:
            count += 1
            current = house[i]

    # 공유기 설치 수가 목표보다 크면 공유기 사이의 거리를 늘림
    if count >= c:
        start = mid + 1
        answer = mid
    # 공유기 설치 수가 목표보다 작으면 공유기 사이 거리 줄임
    else:
        end = mid - 1
```

딱 문제를 보면서 이진 탐색을 어떻게 적용해야 하는지 잘 떠오르지 않아 문제였다.

## 참고

[[백준] 2110: 공유기 설치 (Python)](https://velog.io/@yoonuk/백준-2110-공유기-설치-Python)
