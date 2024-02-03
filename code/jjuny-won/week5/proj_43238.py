def solution(n, times):
    
    start = 1
    end = max(times)*n
    
    while(start<=end):
        mid = (start+end)//2
        cnt =0
        for t in times:
            cnt += mid//t
            #모든 심사관을 거치지 않고 모든 인원 심사 완료했을면 break
            if cnt >=n: 
                break
        #만약에 인원을 초가했을 경우 시간을 줄여야하므로 end = mid -1
        if cnt >= n:
            ans = mid
            end = mid-1
        else:
            start = mid+1
    return ans