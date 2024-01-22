# 백준 1260번

## 접근

가장 먼저 할 것이 DFS, BFS가 무엇인지 생각해야 했다.

깊이, 너비 우선 탐색이라는 건 알고 있었는데 어떻게 진행되는지에 대해 먼저 알아보고 이 문제를 풀려고 했다.

### 1. 깊이 우선 탐색(DFS, Depth-First Search)

최대한 깊이 내려간 뒤, 더이상 깊이 갈 곳이 없을 경우 옆으로 이동

미로찾기의 경우 한 방향으로 갈 수 있을 때까지 쭉 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 그 갈림길부터 다시 다른 방향으로 탐색을 진행
<br>

#### DFS의 구현 원리

DFS에서 데이터를 찾을 때는 “앞으로 찾아 가야할 노드”와 “이미 방문한 노드”를 기준으로 데이터 탐색

특정 노드가 “앞으로 찾아 가야할 노드”라면 계속 검색,

“이미 방문한 노드”면 무시하거나 따로 저장

그래프를 구현

```python
import sys
from collections import defaultdict

# 그래프 구현
graph = defaultdict(list)

n, m, v = map(int, input().split())

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
		graph[b].append(a)

print(graph)
#defaultdict(<class 'list'>, {1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]})
```

#### DFS 구현 방식

기본적으로 “스택/큐”를 활용, “재귀함수”를 통해 구현 가능

#### (1) 리스트를 활용한 DFS 구현

```python
# dfs 리스트 구현
def dfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            graph[node].sort(reverse=True)
            need_visited.extend(graph[node])

    return visited
```

이런 식으로 구현했는데 내가 원하는 결과는 [1, 2, 4, 3] 이지만 출력 결과는 [1, 4, 3, 2] 이었다.

아마 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문하라는 것을 고려하지 않아서 그런 것 같다.

스택을 사용하였기에 마지막 스택에 담은 정점부터 꺼내져 방문되기 때문에 원하는 결과가 나오지 않은 것 같다.

마지막 스택에 담은 정점부터 꺼내는 것에 아이디어를 얻어 내림차순으로 정렬하면 어떨까하는 생각으로 정렬해보았다.

`graph*[node].sort(*reverse*=True)` 그래서 이걸 넣으니 원하는 결과가 출력되었다.

#### (2) 재귀를 통한 DFS 구현

```python
def recursive_dfs(v, visited = []):
    visited.append(v) # 시작 정점 방문
    for w in graph[v]:
        if not w in visited: # 방문 하지 않았으면
            visited = recursive_dfs(w, visited)
    return visited
```

이걸 사용하니 원하는 [1, 2, 4, 3]이 나왔다.

하지만 두 번째 예제를 해보니 [3, 4, 5, 2, 1]가 출력되었다.

정점 번호가 작은 것을 먼저 방문하는 것을 고려하지 않아서 그런거 같다.

그래서 graph[v]를 정렬을 계속하면서 방문하도록 만들었다.

`graph[v].sort()`

<br>

### 2. 너비 우선 탐색 (BFS, Breadth-First Search)

최대한 넓게 이동한 다음, 더 이상 갈 수 없을 때 아래로 이동

루트 노드(임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방식으로 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방식이다.

주로 두 노드 사이의 최단 경로를 찾고 싶을 때 사용

BFS 구현 원리

BFS를 구현하기 위해서 항상 방문하고자 하는 노드와 방문했던 노드를 나누어서 알고리즘을 구성해야 한다.

1. 시작 노드를 방문했던 노드에 삽입
2. 방문할 노드에 시작노드의 Child Node 삽입
3. Child Node를 중심으로 다시 1~2단계를 거쳐 탐색

```python
# bfs 리스트 구현
def bfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)

    while need_visited:
        node = need_visited[0]
        del need_visited[0]

        if node not in visited:
            visited.append(node)
            graph[node].sort()
            need_visited.extend(graph[node])
    return visited
```

작은 노드부터 방문하기위해 `graph[node].sort()` 라고 작성했다.

dfs의 구현했을 때는 맨 끝을 방문했고 bfs의 경우 0번째에 방문하기에 내림차순보다는 오름차순으로 정렬하였더니 맞게 출력되었다.

dfs, bfs를 다른 문제에 적용할 수 있도록 익혀야겠다.

## 참고

아래 블로그에서 잘 설명해줘서 이해하기 편했다.

[DFS 완벽 구현하기 [Python]](https://data-marketing-bk.tistory.com/entry/DFS-완벽-구현하기-파이썬)

[BFS 완벽 구현하기 - 파이썬](https://data-marketing-bk.tistory.com/entry/BFS-완벽-구현하기-파이썬)

<br>

# 백준 12851번

## 접근

일단 예제 1이 어떻게 나오게 되었는지 한번 보면

| 시간 / 방법 | 1번         | 2번         |
| ----------- | ----------- | ----------- |
| 1초         | 4(5 → 4)    | 10(5\*2)    |
| 2초         | 8(4\*2)     | 9(10 → 9)   |
| 3초         | 16(8\*2)    | 18(9\*2)    |
| 4초         | 17(16 → 17) | 17(18 → 17) |

이렇게 두 가지 경우가 가장 빠른 4초로 찾을 수 있는 방법이다.

그래서 4, 2가 출력된다.

이렇게 n에서 이어진 정점을 통해 k까지 가는 방법들을 구한 후 가장 빠른 방법을 구하고 그것의 개수를 구하는 방식으로 구하면 되지 않을까 생각했다.

현재 5에서 갈수 있는 곳은 (3, 4, 10) 여기에서 선택하여 17까지 가는 방법들을 구하는 것이다.

노드 사이의 최단 경로를 구해야 하기에 BFS를 사용하기로 했다.

이전에 구현한 BFS에 적용하여 한번 풀어보겠다.

```python
def bfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)

    while need_visited:
        node = need_visited[0]
        del need_visited[0]

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited
```

어떤 노드를 방문하냐에 따라서 그 다음 노드가 정해지기 때문에 방문할 수 있는 모든 정점들을 만들어서 넣기에는 힘들 것 같아서 돌면서 계속 갱신해주어야 할 것 같다.

내가 생각한 방식은

처음 출발 지점에서 갈수 있는 방법 탐색 →간 곳에서 갈 수 있는 방법 탐색 → 만약 k가 되면 visited의 길이를 배열에 저장, 가장 작은 수, 개수 반환

이렇게 생각했는데 어떻게 구현해야할 지 고민이다.

```python
from collections import defaultdict

n, k = map(int, input().split())
answer = []

# 그래프 구현
graph = defaultdict(list)

def bfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)
    count = 0

    while need_visited:
        node = need_visited[0]
        del need_visited[0]

        graph[node].extend([node - 1, node + 1, node * 2])
        count += 1

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

        if k in graph[node]:
            return len(visited) - count // 2

print(bfs(graph, n))
```

이런 식으로 작성하면 몇초만에 빨리 갈 수 있는지는 구할 수가 있다.

count // 2를 한 이유는 만약 5 → 11을 구한다고 하면 visited에 [5, 4, 6, 10] 이렇게 상관없는 4, 6도 저장되기에 이렇게 작성했다.

그런데 개수는 어떻게 구하지,,?

결국 다른 사람의 코드를 참고해서 했는데 시간초과가 난다.

```python
n, k = map(int, input().split())
dist = [0] * 100001

need_visited = []
need_visited.append(n)

way, count_way = 0, 0

while need_visited:
    node = need_visited[0]
    del need_visited[0]

    if node == k:
        way = dist[node]
        count_way += 1
        continue

    for i in (node - 1, node + 1, node * 2):
        if 0 <= i <= 100000 and (dist[i] == 0 or dist[i] == dist[node] + 1):
            dist[i] = dist[node] + 1
            need_visited.append(i)

print(way)
print(count_way)
```

그래서 리스트 대신 deque()를 이용해보았다.

```python
from collections import deque

n, k = map(int, input().split())
dist = [0] * 100001

need_visited = deque()
need_visited.append(n)

way, count_way = 0, 0

while need_visited:
    node = need_visited.popleft()

    if node == k:
        way = dist[node]
        count_way += 1
        continue

    for i in (node - 1, node + 1, node * 2):
        if 0 <= i <= 100000 and (dist[i] == 0 or dist[i] == dist[node] + 1):
            dist[i] = dist[node] + 1
            need_visited.append(i)

print(way)
print(count_way)
```

dist는 최대 크기의 배열을 만들어 걸리는 횟수를 기록한다.

어떻게 node - 1, node + 1, node \* 2를 방문하면서 할지 고민했는데

`for i in (node - 1, node + 1, node * 2):` 이런 방식으로 반복문을 짜면 되겠구나

그 다음 이 조건문은

`if 0 <= i <= 100000 and (dist[i] == 0 or dist[i] == dist[node] + 1):`

범위 내의 지점이고, 방문하지 않았거나 동일하게 탐색횟수를 가졌다면 탐색하기 위한 조건문이다.

`dist[i] = dist[node] + 1` 방문하고 횟수를 1 늘린다.

너무 어렵따,,,,

## 참고

풀이

[[탐색/BFS] 백준 12851 숨바꼭질 2 - 파이썬(Python)](https://star7sss.tistory.com/540)

deque()

[[파이썬] deque](https://velog.io/@nayoon-kim/파이썬-deque)

<br>

# 프로그래머스 거리두기 확인하기

## 접근

5개의 대기실을 (0, 0)부터 (4, 4)까지 이동하면서 탐색하고 조건에 맞지 않는다면 0을 담고, 아니라면 계속 진행하고 (4, 4)까지 이동했다면 1을 담도록 하게 짜려고 했다.

상하좌우, 그리고 대각선을 고려하기 위해 아래와 같이 방향을 설정하였다.

```python
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]
```

그리고 배열을 순회하면서 주어진 조건이 제대로 부합하는 지 확인하면서 아니라면 0을 리턴 다 순회했다면 1을 반환하도록 작성했는데

`["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]` 경우와

`["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]` 이 경우를 제대로 작동하지 않아서 맨해튼 거리가 2인 경우 X가 있는지 확인하는 코드가 제대로 작동이 안되는 것 같다.

다시 수정해서 코드를 반영하려고 한다,,,ㅎㅎ
