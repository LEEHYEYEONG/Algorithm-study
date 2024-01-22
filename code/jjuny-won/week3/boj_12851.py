from collections import deque


n, k = map(int, input().split())
distance = [0] * 100001
result = 0
cnt = 0
queue = deque([n])

while queue:
    x = queue.popleft()
    if x == k:
        result = distance[x]
        cnt += 1
        continue
    for i in (x - 1, x + 1, x * 2):
        if 0 <= i < 100001 and (distance[i] == 0):
            # 이 부분에서 어떻게 해야할지 모르겠다...
            queue.append(i)

print(result)
print(cnt)
