# 백준 1647번

## 접근

임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다

→ 신장 트리: 모든 노드들 간에 서로 연결은 되어있되 사이클이 존재하지 않는 부분 그래프

간선에 비용이나 가중치가 할당되어있음

신장트리를 만들 수 있는 경우의 수들 중 최소의 간선 비용을 들여서 만들 수 있는 신장 트리 → 최소 신장 트리

따라서 최소 신장 트리를 찾는 크루스칼이라는 알고리즘을 적용하여 문제를 풀어야 겠다고 생각했다.

이 알고리즘을 이용한 문제를 처음 풀어봐서 어떻게 구현하는지 찾아보았다.

### 크루스칼 알고리즘 동작 과정

크루스칼 알고리즘은 가장 적은 간선 비용으로 모든 노드를 연결할 수 있도록 한다.

1. 주어진 모든 간선 정보에 대해 간선 비용이 낮은 순서(오름차순)로 정렬
2. 정렬된 간선 정보를 하나씩 확인하면서 현재의 간선이 노드들 간의 사이클을 발생시키는지 확인
3. 만약 사이클이 발생하지 않은 경우, 최소 신장 트리에 포함시키고 사이클이 발생한 경우, 최소 신장 트리에 포함시키지 않음

사이클이 발생하는지 여부 → 노드들의 부모노드가 같다면 사이클이 발생, 같지 않다면 사이클이 발생하지 않음을 의미

**최소 신장 트리 구현 코드**

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
n, m = map(int, input().split())

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
parent = [i for i in range(n + 1)]

edges = []
result = 0

# 간선을 입력받아 cost를 기준으로 오름차순 정렬
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

edges.sort(key=lambda x: x[2])

# 정렬된 간선을 하나씩 확인
for edge in edges:
    a, b, cost = edge
    # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은것이므로
    if find_parent(parent, a) != find_parent(parent, b):
        # 신장 트리에 간선 추가
        union_parent(parent, a, b)
        result += cost

print(result - max_cost)
```

이렇게 하면 최소 신장 트리의 최소 유지비를 구할 수 있다.

문제는 마을을 분리해야하는 것이다.

구성된 최소 신장 트리에서 비용이 가장 큰 것을 빼면 되지 않을까 생각했다.

그래서 아래와 같이 max_cost를 구해서 result에 빼는 코드를 추가했는데

```python
max_cost = 0
# 정렬된 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은것이므로
    if find_parent(parent, a) != find_parent(parent, b):
        # 신장 트리에 간선 추가
        union_parent(parent, a, b)
        if max_cost <= cost:
            max_cost = cost
        result += cost

print(result - max_cost)
```

주어진 예제는 8이 나왔지만 제출하니 시간초과가 났다.

그리고 오름차순으로 cost를 정렬했기에 비교를 하지 않고 조건에 맞는 마지막 cost가 max_cost가 된다.

시간초과는 입력받는 부분을 수정해서 해결했다.

```python
import sys

input = sys.stdin.readline
```

## 참고

[크루스칼 알고리즘(Kruskal Algorithm) [Python / 파이썬]](https://deeppago.tistory.com/31)

<br>

# 백준 2637번

## 접근

중간부품 5 = 기본 1 _ 2 + 기본 2 _ 2

중간부품 6 = 중간 5 _ 2 + 기본 3 _ 3 + 기본 4 \* 4

완제품 7 = 중간 5 _ 2 + 중간 6 _ 3 + 기본 4 \* 5

= 기본 1 _ 4 + 기본 2 _ 2 + 중간 5 _ 6 + 기본 3 _ 9 + 기본 4 _ 12 + 기본 4 _ 5

= 기본 1 _ 4 + 기본 2 _ 2 + 기본 1 _ 12 + 기본 2 _ 12 + 기본 3 _ 9 + 기본 4 _ 17

= 기본 1 _ 16 + 기본 2 _ 14 + 기본 3 _ 9 + 기본 4 _ 17

필요한 기본 부품의 개수는 `기본 1 * 16 + 기본 2 * 14 + 기본 3 * 9 + 기본 4 * 17` 이다.

이전에 코딩테스트에서도 스킬 트리예제로 이런 문제를 본 적이 있는데 그 때 찾았을 때에 `위상 정렬` 을 사용하면 된다고 들었었다.

제대로 정리를 하지 않았어서 이번에 한번 정리해보려고 한다.

<br>

### 위상 정렬

위상 정렬(Topology Sort)이란 방향 그래프의 모든 노드를 방향성을 모두 지키며 순서대로 나열하는 것을 의미

특정한 노드로 들어오는 간선의 개수를 진입차수라고 한다.

1. 진입차수가 0인 노드를 큐에 담는다.

2. 큐가 비어있을 때까지 다음의 과정을 반복

- 큐에 담긴 노드를 꺼내어 해당 노드에서 출발하는 모든 간선을 그래프에서 제거
- 진입차수가 0인 노드를 큐에 담는다.

모든 원소를 방문하지 않았는데 큐가 비었다는 것은 사이클이 발생했다는 것을 의미

큐에 담기는 노드가 2개 이상인 경우, 위상 정렬된 후의 결과가 여러 개일 수 있음

<br>

1. 진입차수가 0인 노드 1을 큐에 담는다.

| 노드     | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| -------- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0   | 1   | 1   | 2   | 1   | 2   | 1   |

큐: 노드1

<br>

2. 큐에 담긴 노드 1을 꺼내어, 해당 노드에서 출발하는 간선을 모두 그래프에서 제거, 그 후 진입차수가 0인 노드를 큐에 담는다.

| 노드     | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| -------- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0   | 0   | 1   | 2   | 0   | 2   | 1   |

큐: 노드2, 노드5

<br>

3. 큐에 담긴 노드2를 꺼내어, 해당 노드에서 출발하는 간선을 모두 그래프에서 제거, 그 후 진입차수가 0인 노드를 큐에 담는다.

| 노드     | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| -------- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0   | 0   | 0   | 2   | 0   | 1   | 1   |

큐: 노드5, 노드3

<br>

4. 큐에 담긴 노드5를 꺼내고 해당 노드에서 출발하는 간선을 모두 그래프에서 제거, 그 후 진입차수가 0인 노드를 큐에 담는다.

| 노드     | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| -------- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0   | 0   | 0   | 2   | 0   | 0   | 1   |

큐: 노드3, 노드6

<br>

5. 큐에 담긴 노드3을 꺼내고 해당 노드에서 출발하는 간선을 모두 그래프에서 제거, 그 후 진입차수가 0인 노드가 존재하지 않으므로 넘어간다.

| 노드     | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| -------- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0   | 0   | 0   | 1   | 0   | 0   | 1   |

큐: 노드6

<br>

6. 큐에 담긴 노드6을 꺼내어, 해당 노드에서 출발하는 간선을 모두 그래프에서 제거, 그 후 진입차수가 0인 노드를 큐에 담는다.

| 노드     | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| -------- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0   | 0   | 0   | 0   | 0   | 0   | 1   |

큐: 노드4

<br>

7. 큐에 담긴 노드4를 꺼내어, 해당 노드에서 출발하는 간선을 모두 그래프에서 제거, 그 후 진입차수가 0인 노드를 큐에 담는다.

| 노드     | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| -------- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0   | 0   | 0   | 0   | 0   | 0   | 0   |

큐: 노드7

<br>

8. 큐에 담긴 노드7을 꺼내고 7에서 출발하는 간선과 전입차수가 0인 노드가 존재하지 않으므로 큐에서 꺼내진 노드 순서대로 출력하여 위상정렬을 마친다.

**코드**

```python
from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")

topology_sort()
```

이를 원래 문제에 적용하여 코드를 작성해보았다.

여기에서 추가해야할 것은 기본부품인 경우

어떤 부품을 완성하는데 필요한 부품, X에 포함되지 않는 것이 기본부품으로 볼 수 있을 듯 (진입차수가 0인경우)

```python
from collections import deque

n = int(input())
m = int(input())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

# 필요한 부품을 저장하는 리스트
needs = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append([x, k]) # x를 만드는데 y가 k개 필요
    indegree[x] += 1 # 진입차수

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            result.append(i) # 기본부품 리스트
            q.append(i)

    while q:
        now = q.popleft()
        for object, k in graph[now]:
            if now in result: # 기본부품일 경우 목적제품에 +n개
                needs[object][now] += k
            else:
                for i in range(1, n+1):
                    needs[object][i] += needs[now][i]*k
            indegree[object] -= 1
            if indegree[object] == 0:
                q.append(object)

    for i in range(n+1):
        if needs[n][i] > 0:
            print(i, needs[n][i])

topology_sort()
```

## 참고

**위상정렬**

[[Algorithm/Python] 위상 정렬(Topology Sort)란?](https://dmaolon00.tistory.com/entry/AlgorithmPython-위상-정렬Topology-Sort란)

[위상 정렬 개념 & 알고리즘 문제풀이 (백준 2637 장난감 조립, 2252 줄세우기 [파이썬])](https://campkim.tistory.com/10)
