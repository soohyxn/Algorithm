# 구조물이 불가능한지 체크
def check(answer):
    for x, y, a in answer:
        if a: # 보
            # 가능한 경우 = 설치 시점 아래에 기둥이 있는 경우, 설치 시점 아래 오른쪽에 기둥이 있는 경우, 양쪽에 보가 있는 경우
            if [x, y-1, 0] not in answer and [x+1, y-1, 0] not in answer and not ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                return True
        else: # 기둥
            # 가능한 경우 = 맨 밑인 경우, 설치 시점 왼쪽에 보가 있는 경우, 설치 시점에 보가 있는 경우, 설치 시점 아래에 기둥이 있는 경우
            if y != 0 and [x-1, y, 1] not in answer and [x, y, 1] not in answer and [x, y-1, 0] not in answer:
                return True
    return False

def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame:
        if b: # 설치
            answer.append([x, y, a])
            if check(answer): answer.remove([x, y, a]) # 설치 불가능하다면 삭제
        else: # 삭제
            answer.remove([x, y, a])
            if check(answer): answer.append([x, y, a]) # 삭제 불가능하다면 설치
            
    answer.sort() # x좌표 -> y좌표 -> 구조물 종류 순으로 오름차순 정렬
    return answer