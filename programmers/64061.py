def solution(board, moves):
    answer = 0
    n = len(board)
    stack = [] # 바구니
    
    for move in moves:
        for i in range(n):
            if board[i][move-1] != 0:
                if stack and stack[-1] == board[i][move-1]: # 같은 모양 인형이 2개인 경우 인형이 사라진다
                    stack.pop()
                    answer += 2
                else: # 그렇지 않은 경우 바구니에 추가
                    stack.append(board[i][move-1])
                board[i][move-1] = 0
                break
    
    return answer