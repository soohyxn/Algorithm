from collections import defaultdict

def solution(msg):
    words = defaultdict(int) # 사전
    answer = []
    
    # 사전 초기화
    idx = 1 # 색인 번호
    for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        words[a] = idx
        idx += 1
    
    left, right = 0, 0
    while left < len(msg) and right < len(msg):
        if words[msg[left: right+1]] != 0: # 해당 글자가 있는 경우 글자를 늘린다
            right += 1
        else: # 해당 글자가 없는 경우
            answer.append(words[msg[left: right]]) # w 출력
            words[msg[left: right+1]] = idx # 사전에 등록
            idx += 1
            left = right
    answer.append(words[msg[left: right+1]]) # 마지막 글자 출력
        
    return answer