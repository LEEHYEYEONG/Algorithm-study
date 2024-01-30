from itertools import combinations, permutations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        counter = Counter() #이 부분에서 초기화를 해줘야 누적해서 샐 수 있다
        candidates = []
        for menu_li in orders:
            
            res = list(combinations(sorted(menu_li), i))
            #x,w 와 w,x를 같다고 인식시킬 방법
            counter.update(res) #누적해서 count 하기 위한 update 함수
            
        for k,v in counter.items():
                if(v>1):
                    print(k,v)
        # count가 2 이상이면서 가장 많이 등장한 횟수와 같은 조합을 결과에 추가
       

        return sorted(answer)
        



