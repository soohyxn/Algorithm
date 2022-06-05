def solution(stones, k):
    left, right = 1, 200000000 # 이분탐색(징검다리를 건널 수 있는 사람 수)
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0 # 못 건너는 징검다리 수
        
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k: break
            
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
            
    return left