def solution(files):
    sort_file = []
    for i in range(len(files)):
        head_str = ""
        number_str = ""
        digit = False
        for j in files[i]:
            if not j.isdigit() and not digit:
                head_str += j
            elif j.isdigit():
                number_str += j
                digit = True
            else:
                break
    
        sort_file.append([head_str.lower(), int(number_str), i, files[i]])
    print(sort_file)        
    sort_file.sort(key= lambda x:(x[0], x[1], x[2]))

    answer = [i[3] for i in sort_file]
    return answer

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))