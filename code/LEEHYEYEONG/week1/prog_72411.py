from itertools import combinations
from collections import Counter

def solution(orders, course):
    
    # 정렬이 안되어있는 경우 3번째 테스트 케이스 XW, WX로 다르게 저장됨 
    orders = list(map(sorted, orders))
    
    menu = {}
    answer = []

    for i in course:
        combi_list = list()
        for j in orders:
            combi = list(map(lambda x: ''.join(x), combinations(j, i)))
            combi_list.extend(combi)
            menu[i] = Counter(combi_list).most_common()
    
    for i in menu:        
        if menu[i]:
            max_count = menu[i][0][-1]
        
            for menu_name, count in menu[i]:
                if(max_count == 1):
                    continue
                elif(max_count == count):
                    answer.append(menu_name)
        
    return sorted(answer)