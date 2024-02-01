n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

# 공유기 최소 거리 
start = 1
# 공유기 최대 거리
end = house[-1] - house[0]
answer = 0

while (start <= end):
    # 현재 공유기 거리 
    mid = (start + end) // 2
    current = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= current + mid:
            count += 1
            current = house[i]
    
    # 공유기 설치 수가 목표보다 크면 공유기 사이의 거리를 늘림
    if count >= c:
        start = mid + 1
        answer = mid
    # 공유기 설치 수가 목표보다 작으면 공유기 사이 거리 줄임 
    else:
        end = mid - 1

print(answer)

    
