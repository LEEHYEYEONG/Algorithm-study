from heapq import heappush, heappop
# S에 시작해서 T에 끝나는 수업 N개
# 최소의 강의실 => 모든 수업을 들어야 함
# 수업이 끝나야 다음 수업 가능
N = int(input())

input_arr = []

for i in range(N):
    start, end = map(int,input().split()) # 입력 받고
    input_arr.append([start,end]) # 저장

input_arr.sort()
result=[]
heappush(result, input_arr[0][1]) #heapq는 가장 원소 값이 작은 것을 처음으로 빼기 때문에 필요함
# 즉 첫 수업 시작을 제일 빠른 시간표로 하기 위해서!
# print(input_arr, result)

# 만약 result >= input_arr[i][0] 이면 패스하고 다음 순서로
# 다음순서가 <=이면 끝낸다.
# 그 다음 arr[i+1][0]로 넘어가서

for i in range(1,N):
    if result[0] > input_arr[i][0]: # 같이 들을 수 없는 경우
        heappush(result, input_arr[i][1]) # 같이 들을 수 없는 수업의 끝나는 시간을 result에 담는다.
    else: # 같이 들을 수 있는 경우
        heappop(result) # 같이 들을 수 있다면 가장 값이 적은(수업이 가장 빨리 끝나는)값을 없애준다.
        heappush(result, input_arr[i][1])
print(len(result))


