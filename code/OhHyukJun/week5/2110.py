import sys

N,C = map(int,sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)

start, end = 1, arr[-1] - arr[0]

while start <= end:
    mid = (start+end) // 2
    current = arr[0] #공유기 사이의 거리
    count = 1 #공유기 개수 초기화
    for i in range(1,len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i] 
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)