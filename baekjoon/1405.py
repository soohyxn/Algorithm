n, east, west, south, north = map(int, input().split())
dir_per = [east, north, west, south]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
board = [[0] * (2 * n + 1) for _ in range(2 * n + 1)] # 방문 확인 리스트
board[n][n] = 1 # 시작 위치 방문 처리
ans = 0 # 이동 경로가 단순할 확률

def dfs(x, y, cnt, per):
    global ans 

    # 이동 횟수를 다 채운 경우
    if cnt == n:
        ans += per
        return

    # 다음 위치로 이동하기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 2*n+1 and 0 <= ny < 2*n+1 and not board[nx][ny]: # 이동 범위 내에 있으며 아직 방문하지 않는 경우 (= 단순한 이동 경로인 경우)
            board[nx][ny] = 1
            dfs(nx, ny, cnt+1, per * dir_per[i] / 100)
            board[nx][ny] = 0

dfs(n, n, 0, 1)
print(ans)