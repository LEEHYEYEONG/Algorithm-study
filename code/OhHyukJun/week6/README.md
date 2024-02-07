

## 평범한 배낭
- N 개의 물건이 있고 각 물건은 무게 W와 가치 V를 가진다
- 최대 K만큼의 무게만 넣을 수 있음
- 이때 물건 가치의 최대합
- N(1<=N<=100), K(1<=K<=100,000)
- W(1<=W<=100,000), V(0<=V<=1,000)

### 실패 코드
```
import itertools

N,K = map(int,input().split())

arr = {}
W_arr = []
for _ in range(N):
    W, V = map(int,input().split())
    arr[W] = V
    W_arr.append(W)

List = []
for i in range(1,len(W_arr)+1):
    for temp in itertools.combinations(W_arr, i):
        if sum(temp) <= K:
            values = [arr[weight] for weight in temp]  # temp의 각 요소에 해당하는 가치를 리스트로 만듦
            if len(temp) == 1:
                List.extend(values)  # values 리스트 전체를 List에 추가
            else: List.append(sum(values))
        else: break

print(max(List))
```