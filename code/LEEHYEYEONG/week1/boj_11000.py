import sys
import heapq

n = int(sys.stdin.readline())
room_list = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    room_list.append([a, b])

room_list.sort()  

room = [room_list[0][1]]

# heapq는 가장 작은 요소가 heap[0]에 위치한다. 
for i in range(1, n):
    if room[0] <= room_list[i][0]:
        heapq.heappop(room) # 가장 작은 항목 반환
    heapq.heappush(room, room_list[i][1])

# for i in range(1, n):
#     if room[0] <= room_list[i][0]:
#         room.pop(0) 
        
#     room.append(room_list[i][1])
#     room.sort()

print(len(room))