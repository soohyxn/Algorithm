n, east, west, south, north = map(int, input().split())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
dir = [east, south, west, north] 
visited = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
ans = 0 # 이동 경로가 단순할 확률

def dfs(x, y, cnt, per):
    global ans

    # 이동 횟수를 다 채운 경우
    if cnt == n:
        ans += per
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 이동 범위 내에 있으며 아직 방문하지 않는 경우 (= 단순한 이동 경로인 경우)
        if 0 <= nx < 2*n+1 and 0 <= ny < 2*n+1 and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, per * dir[i] / 100)
            visited[nx][ny] = 0

visited[n][n] = 1
dfs(n, n, 0, 1)
print(ans)