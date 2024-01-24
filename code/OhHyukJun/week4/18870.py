N = int(input())
arr = list(map(int,input().split()))
sort_arr = sorted(set(arr))

sort_dict = {}
for i in range(len(sort_arr)):
    sort_dict[sort_arr[i]] = i 
    #정렬했을 때의 인덱스 번호가 현재 자신보다 작은 정수의 수를 의미

for i in range(len(arr)):
    if arr[i] in sort_dict:
        arr[i] = sort_dict[arr[i]]

for i in range(len(arr)):
    print(arr[i],end=' ')