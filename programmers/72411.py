from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        menu = [] # 만들 수 있는 모든 코스
        for order in orders:
            com = list(map(''.join, combinations(sorted(order), c)))
            menu += com
        
        result = Counter(menu).most_common() # 주문 횟수 세기 (많이 주문된 순)
        answer += [menu for menu, cnt in result if cnt >= 2 and cnt == result[0][1]] # 2번 이상 주문되며 가장 많이 주문한 코스만 answer에 추가
    
    return sorted(answer)