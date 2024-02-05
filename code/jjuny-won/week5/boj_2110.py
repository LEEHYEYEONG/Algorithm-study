import sys
n,c = map(int,sys.stdin.readline().split(' '))
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
    
arr.sort()

start = 1 #최소 거리
end = arr[-1] - arr[0] #최대 거리
ans =0
while(start <= end):
    cnt =1 
    cur = arr[0]
    mid = (start+end)//2
    for i in range(1,len(arr)):
        if arr[i] - cur >= mid:
            cnt +=1
            cur=arr[i]
    if cnt >= c:
        start = mid+1
        ans = mid
    else:
        end = mid -1
print(ans)         