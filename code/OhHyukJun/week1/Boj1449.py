N,L = map(int,input().split())
arr = list(map(int,input().split())) #조건대로 입력받기
arr.sort() #오름차순 정렬
left = arr[0] #시작점
tape_count = 1 #출력될 변수
for i in arr[1:]:
    if i in range(left,left+L): #범위 테스트
        continue
    else:
        left = i
        tape_count+=1
print(tape_count)