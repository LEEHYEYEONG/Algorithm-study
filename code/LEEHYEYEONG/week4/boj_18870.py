import sys

n = int(sys.stdin.readline())

# 원래 리스트
number = list(map(int, sys.stdin.readline().split()))

# 중복제거 후 정렬한 리스트
sort_number = sorted(set(number))

index_dict = {value: index for index, value in enumerate(sort_number)}

for num in number:
    print(index_dict[num], end=" ")