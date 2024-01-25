# 백준 10814번

## 접근

이 문제를 보고 나이와 가입 순서를 저장하여 이 두개를 key로 해 출력하도록 만들면 될 것 같았다.

일단은 배열에 나이, 가입한 순서, 이름으로 저장하게 코드를 작성했다.

```python
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    member.append([int(age), i, name])
```

그리고 sort에 key 값을 기준으로 정렬되도록 작성해주었다.

lambda 식을 이용해 age를 기준으로 오름차순, age가 같다면 i를 기준으로 오름차순 정리하도록 하였다.

`member.sort(key= lambda x:(x[0], x[1]))`

## 참고

key를 기준으로 정렬

[[Python] sort()에서의 key lambda 사용하기](https://kingofbackend.tistory.com/98)

<br>

# 백준 10814번

## 접근

### 1) 완전탐색

```python
import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(n):
    count = 0
    for j in range(n):
        if(number[i] > number[j]):
            count+= 1
    answer.append(count)

print(*answer)
```

모든 경우를 돌아서 큰 경우 count에 1을 더해 출력하도록 하는 코드이다.

하지만 시간초과가 난다.

N 제한을 보니 O(NlogN)에 풀이를 해야 하는 듯하다.

### 2) 중복제거, 오름차순 정렬 후 인덱스 이용

일단 생각은 리스트의 중복을 없앤 후, 오름차순으로 정렬 후 현재 인덱스가 Xi > Xj를 만족하는 서로 다른 Xj가 아닐까 하는 생각으로 코드를 작성해보려고 했다.

```python
import sys

n = int(sys.stdin.readline())
# 원래 리스트
number = list(map(int, sys.stdin.readline().split()))

# 중복제거 후 정렬한 리스트
sort_number = sorted(list(set(number)))

for i in range(n):
    print(sort_number.index(number[i]), end=" ")
```

이렇게 작성했는데 index의 시간 복잡도O(n), n번 반복하므로 O(n^2)의 시간 복잡도를 가진다.

index 부분을 수정해야 할 것 같다.

사전에 인덱스를 저장하고 조회하는 경우 시간 복잡도가 O(1)이므로 사전에 미리 인덱스를 사전에 저장하는 방법을 택했다.

```python
# 중복제거 후 정렬한 리스트
sort_number = sorted(set(number))

index_dict = {value: index for index, value in enumerate(sort_number)}

for num in number:
    print(index_dict[num], end=" ")
```

## 참고

시간복잡도

[백준 시간제한과 메모리제한](https://syh39.github.io/algorithm/algorithm_2/)

중복제거

[[python] 파이썬 리스트 중복 제거 방법 3가지](https://blockdmask.tistory.com/543)
