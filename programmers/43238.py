def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n # 심사시간 기준 투포인터
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0 # 심사 가능한 사람 수
        
        for time in times:
            cnt += mid // time
            
        if cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer