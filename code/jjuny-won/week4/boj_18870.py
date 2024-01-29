import sys
n = int(sys.stdin.readline())

array= list(map(int,sys.stdin.readline().split()))
sorted_array = sorted(set(array))
# print(sorted_array)
index_dict = {sorted_array[i]:i for i in range(len(sorted_array))}

# print(index_dict)
for i in array:
    print(index_dict[i], end=" ")