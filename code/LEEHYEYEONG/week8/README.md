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
