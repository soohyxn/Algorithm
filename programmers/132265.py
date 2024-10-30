from collections import Counter

def solution(topping):
    answer = 0 # 롤케이크를 나누는 방법의 수
    divide1 = Counter(topping) # 철수가 가지는 토핑
    divide2 = set() # 동생이 가지는 토핑
    
    # 철수의 토핑을 동생에게 나눈다
    for t in topping:
        divide1[t] -= 1
        divide2.add(t)
        
        if divide1[t] == 0:
            divide1.pop(t)
            
        # 공평하게 나눠진 경우
        if len(divide1) == len(divide2):
            answer += 1
    
    return answer