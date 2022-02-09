def solution(n):
    answer = [[0] * i for i in range(1, n+1)]
    x, y = -1, 0 # 숫자를 채울 위치
    num = 1
    
    for i in range(n): # 방향
        for j in range(i, n): # 숫자를 채울 개수
            if i % 3 == 0: # 하
                x += 1
            elif i % 3 == 1: # 우
                y += 1
            else: # 상
                x -= 1
                y -= 1
                
            answer[x][y] = num
            num += 1
                
    return sum(answer, [])