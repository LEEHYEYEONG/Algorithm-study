# 백준 1913번

## 접근

n\*n의 배열의 중앙에서 시작하면서 이동하며 숫자를 채워나가는 방식
<br>
여기까지는 생각했지만 어떻게 채워나가야 하는지 몰라서 찾아봤으나 다 이해가 안되었음

### 방향 설정

```python
# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
```

해결한 코드를 보면 방향 설정하는 것도 이해가 잘 안되었는데 현재 내가 만든 배열은 2차원 배열이라서 `n_list[x][y]` 라고 할 때 반대로 생각했어야 했다.

```python
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
```

우 -> dx[0]: 1 증가, dy[0]: 변화 x <br>
하 -> dx[1]: 변화x, dy[1]: 1 증가 (이것도 처음에는 1 감소로 생각했다.) <br>
좌 -> dx[2]: 1 감소, dy[2]: 변화 x <br>
상 -> dx[3]: 변화x, dy[3]: 1 감소 (이것도 처음에는 1 증가로 생각했다.) <br>

그래서 처음에는 이렇게 생각했었는데 이렇게 작성하면 `n_list[y][x]`로 바꾸어서 생각해야 한다.

### 채우기

```python
while True:
    for i in range(4):
        for _ in range(len):
            x += dx[i]
            y += dy[i]
            num += 1
            n_list[x][y] = num
            if num == m:
                ans = [x+1, y+1]

    if x==y==0:
        break
    x -= 1
    y -= 1
    len += 2

```

전체 방향 (4방향)에 대해 루프를 진행하고 하나의 루프가 끝나면 길이를 2씩 증가해 나선형으로 만든다.
<br>
그리고 1씩 감소한 이유는 루프 종료의 조건을 위해 만들어 둔 것 같다.

## 문제

m이 1인 경우는 ans를 대입하는 과정없이 출력하므로 런타임에러(NameError)가 난다.

그래서 아래와 같이 처리를 했다.

```python
if m == 1:
    ans = [x+1, y+1]
```

![Alt text](image.png)
난리부르스치고 맞았다.

#### 참고 블로그

https://www.acmicpc.net/problem/1913

# 백준 14719번

## 접근

w만큼 반복하면서 이전의 가장 높은 높이보다 더 큰 높이가 나온다면 이때까지 temp에 모인 빗물을 volume에 더하고 아니라면 temp에 계속 더해나간다.

그리고 max_height를 갱신해나간다.

```python
w, h = map(int, input().split())
map_list = list(map(int, input().split()))

temp = 0
volume = 0
max_height = map_list[0]

for i in range(w):
    if(max_height <= map_list[i]):
        volume += temp
        temp = 0
        max_height = map_list[i]
    else:
        temp += (max_height - map_list[i])

print(volume)
```

이렇게 짜면 문제점이 하나의 웅덩이만 가능하다.

예제1, 3은 원하는 출력이 나오고 예제 2는 원하는 값이 나오지 않는다.

예제 2에서 3만큼 쌓이고 max_height가 현재 4이므로 2를 만났을 때 빗물을 더할 수 없다는게 문제점이다.

그리고 max_list[0]으로 초기에 max_height를 설정해두었는데 이것보다 작지만 전에 빗물보다는 크다면 제대로 구할 수 없다.

그래서 투포인터를 사용해 풀이를 진행했다.

맨왼쪽과 맨오른쪽에 pointer를 두고 중앙으로 이동하고 최대 높이의 막대까지 기둥 최대 높이와 현재 높이와의 차이만큼 volume을 더한다.

```python
h, w = map(int, input().split())
map_list = list(map(int, input().split()))

volume = 0
left, right = 0, w - 1
max_left, max_right = map_list[left], map_list[right]

while left < right:
    max_left, max_right = max(map_list[left], max_left), max(map_list[right], max_right)

    if max_left <= max_right:
        volume += max_left - map_list[left]
        left += 1
    else:
        volume += max_right - map_list[right]
        right -= 1

print(volume)
```

w, h를 굳이 안받아도 될것 같다.

이와 비슷한 문제를 이전에 푼 적이 있어서 투포인터 풀이를 떠올랐는데 제대로 구현하지 못해서 이전에 푼 걸 참고했다.

제대로 기억하기 위해서 예제 2를 차근차근 적용해보겠다.

|     | left, right | max_left, max_right | volume                   |           |
| --- | ----------- | ------------------- | ------------------------ | --------- |
| 1   | 3, 2        | 3, 2                | volume = 0 + (2 - 2) = 0 | right = 1 |
| 2   | 3, 1        | 3, 2                | volume = 0 + (2 - 1) = 1 | right = 1 |
| 3   | 3, 1        | 3, 2                | volume = 1 + (2 - 1) = 2 | right = 4 |
| 4   | 3, 4        | 3, 4                | volume = 2 + (3 - 3) = 2 | left = 1  |
| 5   | 1, 4        | 3, 4                | volume = 2 + (3 - 1) = 4 | left = 2  |
| 6   | 2, 4        | 3, 4                | volume = 4 + (3 - 2) = 5 | left = 3  |
| 7   | 3, 4        | 3, 4                | volume = 5 + (3 - 3) = 5 | left = 4  |

<br>

## 참고

### 투포인터

https://learning-e.tistory.com/37

### 풀이

https://velog.io/@kynel/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B9%97%EB%AC%BC-%ED%8A%B8%EB%9E%98%ED%95%91

<br>

# 프로그래머스 문자열 압축

## 접근

일단 하나씩 자르는 경우를 구현해보았다.

```python
def solution(s):
    #s = list(s)
    stack = []
    char = ''
    for i in s:
        if(stack and stack[-1] != i):
            char += stack[-1] if stack.count(stack[-1]) == 1 else (str(stack.count(stack[-1])) + stack[-1])
            stack.clear()
        stack.append(i)

    char += stack[-1] if stack.count(stack[-1]) == 1 else (str(stack.count(stack[-1])) + stack[-1])
    print(char)

    return len(char)

print(solution("aabbaccc"))
```

하나씩 자르는 경우 전의 꺼만 비교하면 되어서 stack[-1]을 비교해서 다르다면 char에 count를 넣고 stack을 비운다.

문자열이 여러개 인 경우 어떻게 압축할까?

만약 2개인 경우 슬라이싱에서 [0:2] → [2:4] 이런식으로 비교해나가면서 할 수 있지 않을까해서 원래 쓴 코드에 적용해서 작성해보았다.

```python
for i in range(1, len(s)//2 + 1):
    for j in range(0, len(s), i):
				string.append(s[j:j+i])
```

이런 식으로 하면 차례대로 문자열을 나누어서 저장할 수 있다.

이전의 풀이를 이 슬라이싱한 문자열로 대체해서 비교하였다.

자르는 문자열의 크기는 s의 절반을 넘을 수 없으니 `len(s) // 2 + 1` 로 반복되는 횟수를 지정했다.

1을 생략하기 위한 로직 부분은 따로 함수로 구현하였다.

```python
def count_stack(stack):
    if(stack.count(stack[-1]) == 1):
        char = stack[-1]
    else:
        char = (str(stack.count(stack[-1])) + stack[-1])
    stack.clear()

    return char
```

```python
for i in range(1, len(s)//2 + 1):
        for j in range(0, len(s), i):
            if(string and string[-1] != s[j:j+i]):
                char+= count_stack(string)
            string.append(s[j:j+i])

        char+= count_stack(string)
        answer.append(len(char))
        char = ''
```

만약에 이전에 문자열과 다르면 count_stack 함수를 이용해서 char에 더한다. 이렇게 하면 마지막 string에 담긴 것을 추가할 수 없어서

`char+= count_stack(string)` j 반복문이 돈 후 해주었다.

answer에 char의 길이를 추가해준 후 char를 초기화했다.

_`return_ min(answer)` 그리고 answer 중 가장 작은 수를 리턴한다.
<br>

## 문제

테스트 케이스 중 5번이 런타임에러가 났는데 s가 1일 경우 for문을 돌지 않고 answer이 비어있기에 에러가 난다.

그래서 아래 코드를 추가해주었다.

```python
if(len(s) == 1):
		return 1
```
