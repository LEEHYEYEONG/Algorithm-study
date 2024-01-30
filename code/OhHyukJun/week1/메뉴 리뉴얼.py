def combination(arr,n):
    result = []
    if len(arr) < n: #orders의 길이가 course보다 작으면 빈 배열 출력
        return result
    if n == 1: #course를 다 돌면 최종 결과를 출력
        return [[i] for i in arr]
    else:
        for i in range(len(arr)):
            rest = arr[i+1:]
            for j in combination(rest,n-1):
                result.append([arr[i]]+j)
        return result

def count(combos):
    count = {}
    for i in combos:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
    
def solution(orders, course):
    answer = []
    orders = [''.join(sorted(i)) for i in orders] # orders를 알파벳 순으로 정렬 후 ""로 구분 ["A","B"]
    for i in course:
        combos=[]
        for j in orders:
            combinations = combination(list(j),i)
            sort_combos = [''.join(combo) for combo in combinations]
            combos.extend(sort_combos)
        counts = count(combos) #counts는 리스트 {"ABC":1} 형태
        if counts:
            max_count = max(counts.values())
            if max_count > 1:
                for menu,order_count in counts.items(): #리스트 요소가 items 안에 있다면
                    if order_count == max_count:
                        answer.append(menu)
    answer = sorted(answer)
    return answer