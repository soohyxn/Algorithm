n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
answer = 0

def clean(x, y, z):
    global answer

    # 1. 현재 칸이 아직 청소되지 않은 경우, 현채 칸을 청소한다
    if board[x][y] == 0:
        board[x][y] = 2
        answer += 1
    
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    for _ in range(4):
        zd = (z + 3) % 4
        xd = x + dx[zd]
        yd = y + dy[zd]
        
        if xd < 0 or xd >= n or yd < 0 or yd >= m:
            continue
        
        # 3-1. 반시계 방향으로 90도 회전한다
        z = zd

        # 3-2. 앞쪽 칸이 청소되지 않은 빈 칸인 경우, 한 칸 전진한다
        if board[xd][yd] == 0:
            clean(xd, yd, zd)
            return
    
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    zb = (z + 2) % 4
    xb = x + dx[zb]
    yb = y + dy[zb]

    # 2-2. 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다
    if board[xb][yb] == 1:
        return
    # 2-1. 한 칸 후진할 수 있다면 한 칸 후진한다
    else:
        clean(xb, yb, z)

clean(r, c, d)
print(answer)