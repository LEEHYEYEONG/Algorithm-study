N = int(input())
arr = list(map(int, input().split()))
M = int(input())

start, end = 0, max(arr) #이진 탐색의 시작값과 끝값을 설정

while start <= end:
    mid = (start + end) // 2 #탐색 범위의 중간값
    sum_arr = 0 
    for i in arr:
        if i <= mid:
            sum_arr += i #중앙값보다 작으면 그대로 더하기
        else:
            sum_arr += mid #중앙값보다 크면 상환액을 더해줌
            
    if sum_arr <= M: 
        start = mid + 1
    else: 
        end = mid - 1

print(end)
