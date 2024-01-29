n = int(input())

array=[]

for i in range(n):
    data=input().split()
    array.append((int(data[0]),data[1]))


array=sorted(array,key=lambda user:user[0])
 
for user in array:
    print(user[0],user[1])