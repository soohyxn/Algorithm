# 제거할 블록 찾기
def pop(m, n, board):
    delete = []
    
    for x in range(m-1):
        for y in range(n-1):
            if board[x][y] == board[x][y+1] == board[x+1][y] == board[x+1][y+1] != '':
                delete.extend([(x, y), (x, y+1), (x+1, y), (x+1, y+1)])
                    
    return delete

def solution(m, n, board):
    board = [list(b) for b in board]
    answer = 0 # 제거된 블록 개수
    
    while True:
        delete = pop(m, n, board) # 제거할 블록 찾기

        if len(delete) == 0: # 제거할 블록이 없는 경우
            break
            
        answer += len(set(delete))
        
        # 제거할 블록 위치는 빈칸으로
        for x, y in delete:
            board[x][y] = ''

        # 블록을 위에서 아래로 떨어지기
        while True:
            move = 0
            
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and not board[i+1][j]:
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        move += 1
            
            if move == 0: break
        
    return answer