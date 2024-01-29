def solution(files):
    answer = []
    
    for file in files:  
        head, num, tail = '', '', ''
        
        for i in range(len(file)):
            if file[i].isdigit():  
                num += file[i]
            else:
                if not num:
                    head += file[i]
                else:
                    tail = file[i:]
                    break
        
        answer.append((head, num, tail))
        # print(answer)

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
    answer = [''.join(t) for t in answer]

    return answer


