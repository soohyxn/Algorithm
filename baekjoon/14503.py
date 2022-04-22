N, M = map(int, input().split())
r, c, d= map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
ans = 0 # 청소하는 칸의 개수

def clean(x, y, d):
    global ans

    # 현재 위치를 청소한다
    if board[x][y] == 0:
        board[x][y] = 2
        ans += 1

    # 현재 위치에서 인접한 칸을 탐색한다
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        # 현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 왼쪽 방향으로 회전한 다음 한 칸을 전진한다
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd # 그렇지 않을 경우, 왼쪽 방향으로 회전한다
    
    # 2-a번 단계가 연속으로 네 번 실행되었을 경우
    bd = (d + 2) % 4
    bx = x + dx[bd]
    by = y + dy[bd]
    if board[bx][by] == 1: # 뒤쪽이 벽이라면 작동을 멈춘다
        return
    clean(bx, by, d) # 그렇지 않다면, 한 칸 후진한다

clean(r, c, d)
print(ans)