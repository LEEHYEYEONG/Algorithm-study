import heapq,sys
n = int(sys.stdin.readline())
arr=[]
for  i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))   
arr.sort()
# print(arr)
room = []
heapq.heappush(room, arr[0][1])


for i in range(1, n):
    if arr[i][0] < room[0]: # room  보다 회의 시작 시간이 빠르면
        heapq.heappush(room, arr[i][1]) # 새로운 강의실 개설
    else: # 한 강의실 이어서 사용
        heapq.heappop(room) #pop 후 갱신된 (최신 시간 )으로 바꾸기
        heapq.heappush(room,arr[i][1])

    # print("room",room)
print(len(room))
