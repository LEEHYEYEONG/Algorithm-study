H,W = map(int,input().split())
arr = [[0]* W for _ in range(H)]
heights = list(map(int,input().split()))
count = 0

for j in range(W):
    for i in range(heights[j]):
        arr[H-i-1][j] = 1

for i in range(1,W-1): #양극단 값은 count에서 제거
    left = max(heights[:i]) #현재까지 블록 최대 높이
    right = max(heights[i+1:]) #이훙 블록 최대 높이
    min_height = min(left,right) #비교해서 최솟값을 최소 높이로 저장

    if min_height > heights[i]: #불록 높이보다 물의 높이가 크다면
        count += min_height - heights[i]

print(count)

