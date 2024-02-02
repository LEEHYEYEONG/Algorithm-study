def solution(n, times):
    answer = 0

    # 가장 짧은 심사시간
    start = 1
    # 가장 긴 심사시간에게 n명이 심사 
    end = max(times) * n

    while (start <= end):
        mid = (start + end) // 2 # 심사한 시간 
        count = 0 # 심사한 사람의 수 
        for i in range(len(times)):
            count += mid // times[i]
            if count >= n: 
                break
        
        # 심사한 사람의 수가 n보다 많은 경우 
        if count >= n:
            end = mid - 1 # 시간을 줄인다 
            answer = mid
            
        # 심사한 사람의 수가 n보다 적은 경우
        else:
            start = mid + 1 # 시간을 늘린다 

    return answer

print(solution(n=6, times=[7, 10]))