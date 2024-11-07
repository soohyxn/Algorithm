def solution(n, s):
    
    # 최고의 집합이 존재하지 않는 경우 바로 리턴
    if n > s:
        return [-1]
    
    num, remain = s//n, s%n
    answer = [num] * n
    
    # 최고의 집합 구하기
    if remain != 0:
        for i in range(n):
            answer[i] += 1
            remain -= 1
            if remain == 0:
                break
    
    answer.sort()
    return answer