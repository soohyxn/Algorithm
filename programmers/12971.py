def solution(sticker):
    size = len(sticker)
    
    # 스티커가 1개인 경우 바로 리턴
    if size == 1:
        return sticker.pop()
    
    # 1. 0번째 스티커를 떼는 경우
    dp1 = [0] + sticker[:-1]
    for i in range(2, size):
        dp1[i] = max(dp1[i-1], dp1[i-2] + dp1[i])

    # 2. 1번째 스티커를 떼는 경우
    dp2 = [0] + sticker[1:]
    for i in range(2, size):
        dp2[i] = max(dp2[i-1], dp2[i-2] + dp2[i])
    
    return max(dp1[-1], dp2[-1])