h,w = map(int,input().split())
arr = list(map(int,input().split()))

#가장 큰 수를 기준으로 나눈다

result=0

# 범위를 w로 했을 경우 첫번째 요소의 left, 마지막 요소의 right를 구할 수 없기 때문에

for i in range(1,w-1):
    left = max(arr[:i])
    right = max(arr[i+1:])
    m = min(left,right)
    if(m>arr[i]):
        result += m-arr[i]
print(result)