N = int(input())
arr = []
for _ in range(N):
    age, name = input().split()
    arr.append((int(age),name))

arr.sort(key=lambda x : x[0])

for i in range(len(arr)):
    print(arr[i][0], arr[i][1])