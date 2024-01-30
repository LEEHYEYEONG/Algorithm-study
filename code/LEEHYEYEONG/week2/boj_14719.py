h, w = map(int, input().split())
map_list = list(map(int, input().split()))

volume = 0
left, right = 0, w - 1
max_left, max_right = map_list[left], map_list[right]

while left < right:
    max_left, max_right = max(map_list[left], max_left), max(map_list[right], max_right)

    if max_left <= max_right:
        volume += max_left - map_list[left]
        left += 1
    else:
        volume += max_right - map_list[right]
        right -= 1

print(volume)

