from collections import defaultdict

def solution(gems):
    n = len(set(gems))
    left, right = 0, 0 # 투포인터
    jewelry = defaultdict(int) # 구매할 보석별 개수
    jewelry[gems[0]] = 1
    answer = [0, len(gems)-1]
    
    while left < len(gems) and right < len(gems):
        # 모든 종류의 보석을 구매할 수 있는 경우
        if len(jewelry) == n:
            if right - left < answer[1] - answer[0]: # 가장 짧은 구간인 경우
                answer = [left, right]
            # 보석 제거
            if jewelry[gems[left]] == 1:
                del jewelry[gems[left]]
            else:
                jewelry[gems[left]] -= 1
            left += 1
        # 모든 종류의 보석을 구매할 수 없는 경우
        else:
            right += 1
            if right == len(gems): break
            jewelry[gems[right]] += 1 # 보석 추가
        
    return [answer[0]+1, answer[1]+1]