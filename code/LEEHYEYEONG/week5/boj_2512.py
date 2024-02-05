n = int(input())
money = list(map(int, input().split()))
max_sum = int(input())

def add(max_number, money):
    result = 0
    for i in money:
        if(i < max_number):
            result += i
        else:
            result += max_number
    
    return result 

# 모든 요청이 배정될 수 있는 경우 
if(sum(money) <= max_sum):
    print(max(money))
# 모든 요청이 배정되지 않는 경우 
else:
    start = 1
    end = max(money)
    while start <= end:
        mid = (start + end) // 2
        if(add(mid, money) <= max_sum):
            start = mid + 1
        else:
            end = mid - 1
    print(end)