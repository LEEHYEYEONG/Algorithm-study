# 입력
n, l = map(int, input().split())
location = sorted(list(map(int, input().split())))

# 테이프 개수
tape = 1
pointer = location[0] + l - 0.5

for i in range(1, n):
    if(pointer >= location[i] + 0.5):
        continue
    pointer = location[i] + l - 0.5
    tape += 1

print(tape)




