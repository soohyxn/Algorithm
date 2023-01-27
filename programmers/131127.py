from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):
        cnt = Counter(discount[i: i+10]) # 10일간 제품별 수량
        
        for j in range(len(want)):
            if cnt[want[j]] != number[j]: # 원하는 제품과 수량이 일치하지 않는 경우 종료
                break
        else:
            answer += 1        
                
    return answer