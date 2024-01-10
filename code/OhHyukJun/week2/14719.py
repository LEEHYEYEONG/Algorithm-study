H,W = map(int,input().split())
arr = [[0]* W for _ in range(H)]
heights = list(map(int,input().split()))
count = 0

for j in range(W):
    for i in range(heights[j]):
        arr[i][j] = 1

for i in range(H):
    print(arr[i])
print(heights)