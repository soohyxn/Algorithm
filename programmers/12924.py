def solution(n):
    answer = 1
    
    for i in range(1, n//2+1):
        num = i
        for j in range(i+1, n+1):
            num += j
            if num == n:
                answer += 1
                break
            elif num > n:
                break
                
    return answer