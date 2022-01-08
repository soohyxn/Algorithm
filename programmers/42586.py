import math

def solution(progresses, speeds):
    answer = []
    day = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)] + [1e9] # 작업 완료 날짜 계산
    now = day[0] # 현재 작업 날짜
    cnt = 1 # 배포될 기능 수
    
    for i in range(1, len(day)):
        if now < day[i]: # 현재 작업 날짜보다 크다면 현재 작업까지 배포
            answer.append(cnt)
            # 초기화
            now = day[i]
            cnt = 1
        else: # 현재 작업 날짜보다 작다면 현재 배포에 포함
            cnt += 1
            
    return answer