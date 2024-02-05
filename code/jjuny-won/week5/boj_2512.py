

n = int(input())
arr = list(map(int,input().split()))
limit = int(input())

start = 0
end = max(arr)
result =0

while(start <= end):
    total = 0
    mid = (start + end)//2
    for x in arr:
        # 지역의 예산안이 상한액보다 크거나 같으면
        if x>=mid:
            total += mid 
        # 지역의 예산안이 상한액보다 작으면
        else:
            total += x 
    #limit 보다 클경우 end 를 줄여야함 -> mid 도 줄어든다
    print(mid,total)
    if total > limit: 
        end = mid -1
    # total 이 limit 보다 작을 경우, start 를 키워야한다
    else:
        result = mid
        start= mid+1
print(result)