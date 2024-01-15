def count_stack(stack):
    if(stack.count(stack[-1]) == 1):
        char = stack[-1]
    else:
        char = (str(stack.count(stack[-1])) + stack[-1])
    stack.clear()
    
    return char

def solution(s):
    string = []
    answer = []
    char = ''

    if(len(s) == 1):
        return 1

    for i in range(1, len(s)//2 + 1):
        for j in range(0, len(s), i):
            if(string and string[-1] != s[j:j+i]):
                char+= count_stack(string)
            string.append(s[j:j+i])

        char+= count_stack(string)
        answer.append(len(char))
        char = ''
            
    return min(answer)

print(solution("xababcdcdababcdcd"))