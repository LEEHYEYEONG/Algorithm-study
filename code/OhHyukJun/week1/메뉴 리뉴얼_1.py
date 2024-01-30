from itertools import combinations

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
            combis = combinations(list(j),i) #라이브러리 사용
            sort_combos = [''.join(combo) for combo in combis]
            combos.extend(sort_combos)
        counts = count(combos) #counts는 리스트 {"ABC":1} 형태
        if counts:
            max_count = max(counts.values())
            if max_count > 1:
                for menu,order_count in counts.items():
                    if order_count == max_count:
                        answer.append(menu)
    answer = sorted(answer)
    return answer