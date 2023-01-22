from itertools import combinations_with_replacement as cwr

def solution(n, info):
    answer = [-1]
    max_diff = -1 # 최대 점수 차이
    
    # 중복조합으로 과녁점수 경우의 수를 구한다
    for com in cwr(range(11), n):
        score = [0] * 11 # 라이언 과녁점수
        apeach, lion = 0, 0 # 라이언, 어피치 최종 점수
        
        for c in com:
            score[10 - c] += 1
        
        # 최종 점수 구하기
        for i in range(11):
            # 아무도 과녁을 맞추지 못한 경우
            if info[i] == score[i] == 0:
                continue
            # 어피치가 점수를 얻는 경우
            elif info[i] >= score[i]:
                apeach += 10 - i
            # 라이언이 점수를 얻는 경우
            else:
                lion += 10 - i
                
        # 라이언이 우승할 수 있다면 answer 갱신
        if lion > apeach:
            diff = lion - apeach
            if diff > max_diff:
                max_diff = diff
                answer = score
    
    return answer