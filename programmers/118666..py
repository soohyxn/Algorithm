from collections import defaultdict

def solution(survey, choices):
    answer = ''
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    result = defaultdict(int) # 유형별 점수
    
    # 유형별 점수 구하기
    for i in range(len(survey)):
        result[survey[i][choices[i] // 4]] += score[choices[i]]

    # 성격 유형 구하기 - 점수, 사전순
    answer += 'R' if result['R'] >= result['T'] else 'T'
    answer += 'C' if result['C'] >= result['F'] else 'F'
    answer += 'J' if result['J'] >= result['M'] else 'M'
    answer += 'A' if result['A'] >= result['N'] else 'N'
    
    return answer