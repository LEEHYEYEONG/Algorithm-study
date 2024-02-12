def solution(N, number):
    dp = []
    
    for i in range(1,9):
        dp.append(int(str(N)*i))
    
    print(dp)
    answer = 0
    return answer