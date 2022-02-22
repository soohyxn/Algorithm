from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = [] # 각 문의 조건을 만족하는 사람 수
    info_dict = defaultdict(list) # 가능한 모든 지원 경우
    
    # 가능한 모든 지원 경우 구하기
    for i in info:
        tmp = i.split()
        key = tmp[:-1] # 키 - 언어, 직군, 경력, 소울푸드
        value = tmp[-1] # 값 - 점수
        
        # 모든 조합 생성
        for j in range(5):
            for com in combinations(key, j):
                info_dict[''.join(com)].append(int(value))
    
    # 각 키의 값 정렬
    for key in info_dict:
        info_dict[key].sort()
    
    # 문의 조건을 만족하는 사람 수 구하기
    for q in query:
        tmp = q.split(' ')
        key = tmp[:-1] # 키 - 언어, 직군, 경력, 소울푸드
        value = tmp[-1] # 값 - 점수
        
        # and, - 삭제
        while 'and' in key:
            key.remove('and')
        while '-' in key:
            key.remove('-')
            
        qu_key = ''.join(key)
        if qu_key in info_dict: # 가능한 지원 경우에 있다면 이분탐색으로 문의 조건을 만족하는 사람 수를 구한다
            scores = info_dict[qu_key]
            if scores:
                enter = bisect_left(scores, int(value)) # 값을 넘지 않는 사람 수
                answer.append(len(scores) - enter)
        else: # 가능한 지원 경우에 없다면 문의 조건을 만족하는 사람은 0명
            answer.append(0)
    
    return answer