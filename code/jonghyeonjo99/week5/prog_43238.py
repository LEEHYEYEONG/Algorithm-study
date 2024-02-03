def solution(n, times):
    answer = float("inf")
    
    left = 0
    right = (n+1) * max(times)
    mid = 0
    
    while(left <= right):
        mid = (left + right) // 2
        count = 0
        for time in times:
            accept_people = mid // time
            count += accept_people
            
        if(count < n):
            left = mid + 1
        elif(count >= n):
            right = mid - 1
            if(mid < answer):
                answer = mid
                
    return answer