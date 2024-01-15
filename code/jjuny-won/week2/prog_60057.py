def solution(s):
    answer=[]

   
    for i in range(1, len(s)+1):
        sen = ''
        cnt = 1
        tmp=s[:i] #이 부분을 반복문에 넣었어서 조금 헤맸다

        for j in range(i, len(s)+i, i):
            
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    sen = sen + str(cnt)+tmp
                else:
                    sen = sen + tmp
                    
                tmp=s[j:j+i]
                cnt = 1
        #print(sen)
                
        answer.append(len(sen))
        

    return min(answer)
