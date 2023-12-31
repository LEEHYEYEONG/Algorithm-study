import sys
import heapq
from collections import deque

n = int(sys.stdin.readline().rstrip())
classes = []
ends = []

for i in range(n):
  lecture = list(map(int,sys.stdin.readline().rstrip().split()))
  classes.append(lecture)

classes.sort(key= lambda x : (x[0],x[1]))

# start = classes[0][0]
end = classes[0][1]

# ends.append(end)

classes = deque(classes)
classes.popleft()

# for s, t in classes:
#   for i in range(len(ends)):
#     if(s < ends[i]):
#       ends.append(t)
#       ends.sort()
#       break
#     else: #(s >= ends[i])
#       ends[i] = t
#       ends.sort()
#       break

heapq.heappush(ends,end)

for i in range(len(classes)):
  if(ends[0] > classes[i][0]):
    heapq.heappush(ends, classes[i][1])
  else:
    heapq.heappop(ends)
    heapq.heappush(ends, classes[i][1])

print(len(ends))
