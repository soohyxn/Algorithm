def solution(n):
    # n이 1, 2인 경우 바로 리턴
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    
    # 경우의 수 계산
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567