def solution(rows, columns, queries):
    board = [[i for i in range(r*columns+1, (r+1)*columns+1)] for r in range(rows)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
    answer = [] # 가장 작은 숫자 리스트
    
    for lx, ly, rx, ry in queries:
        lx -= 1; ly -= 1; rx -= 1; ry -= 1 # 인덱스 맞추기
        x, y, before, d = lx, ly, board[lx][ly], 0 # 현재 위치, 값, 방향
        ans = 1e9 # 가장 작은 숫자
        
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < lx or nx > rx or ny < ly or ny > ry: # 이동 가능 범위를 벗어나면 방향을 바꾼다
                d += 1
                continue
                
            board[nx][ny], before = before, board[nx][ny] # 값 이동
            ans = min(ans, board[nx][ny]) # 가장 작은 수 갱신
            x, y = nx, ny # 위치 이동
            
            if x == lx and y == ly: # 회전이 끝나면 멈춘다
                break
        
        answer.append(ans)
            
    return answer