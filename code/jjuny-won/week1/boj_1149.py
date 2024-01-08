n,l = map(int,input().split())
pos = list(map(int,input().split()))

#필요한 테이프의 길이 -> n

pos.sort()

cnt =1
start = pos[0]
for loc in pos:
    if loc in range (start, start+l):
        continue
    else:
        start = loc
        cnt+=1
        
print(cnt)

       