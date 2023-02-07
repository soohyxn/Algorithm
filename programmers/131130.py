def solution(cards):
    answer = []
    
    # 모든 상자그룹을 구한다
    for i in range(len(cards)):
        group = []
        j = i
        
        # 열어야 하는 상자가 이미 열려 있을 때까지 상자를 연다
        while cards[j] not in group:
            group.append(cards[j])
            j = cards[j] - 1
        
        # 새로운 상자그룹이라면 추가 
        if set(group) not in answer:
            answer.append(set(group))
        
    answer.sort(key = lambda x: -len(x)) # 길이 역순 정렬
        
    return len(answer[0]) * len(answer[1]) if len(answer) > 1 else 0