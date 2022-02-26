def solution(board):
    n, m = len(board), len(board[0])
    
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1 # dp
    
    answer = max([max(b) for b in board]) # 정사각형 최대 길이

    return answer ** 2