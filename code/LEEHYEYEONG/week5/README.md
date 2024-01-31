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
