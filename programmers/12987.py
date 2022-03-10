def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    # B가 절대 승리할 수 없는 경우
    if A[-1] > B[0]:
        return answer
    
    # 최대 승점 구하기
    i = 0
    for a in A:
        if a < B[i]:
            answer += 1
            i += 1
    
    return answer