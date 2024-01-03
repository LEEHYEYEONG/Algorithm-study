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
