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
