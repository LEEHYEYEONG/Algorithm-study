
n = int(input())
find_n = int(input())

arr = [[0]*n for _ in range(n)]

num = n*n

# 첫번째 접근 -> x

# for j in range(n):
#     for i in range(n):
#         arr[i][j] = num
#         num -=1
# print(arr)

#--------------------------

#두번째 접근
i, j = 0, 0
cnt = n

while cnt > 0:
    if i == 0 or j == 0:
        for k in range(cnt):
            arr[i][j] = num
            num -= 1
            i += 1
    else:
        for k in range(cnt):
            i -= 1
            arr[i][j] = num
            num -= 1
        for k in range(cnt):
            j -= 1
            arr[i][j] = num
            num -= 1
        cnt -= 1
        for k in range(cnt):
            i += 1
            arr[i][j] = num
            num -= 1

for row in arr:
    print(row)

# 2번 문제 시도 후 index 에러 발생, 로직 자체가 너무 비효율적 