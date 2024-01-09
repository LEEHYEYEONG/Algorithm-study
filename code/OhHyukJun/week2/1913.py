N = int(input())
Num = int(input())
Num_dict = {(i, 1): N**2+1-i for i in range(1, N+1)}
Num_dict_1 = {(N, j+1): N**2+1-j-N for j in range(1, N)}

print(Num_dict,Num_dict_1)
#1,1 2,1 3,1 3,2 3,3 2,3 1,3 1,2 2,2