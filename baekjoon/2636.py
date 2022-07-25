from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
ans = [] # 각 시간마다 녹은 치즈 개수

def bfs(i, j):
    queue = deque([[i, j]])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    cnt = 0 # 녹은 치즈 개수

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위이며 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 가장 자리 치즈인 경우 녹는다
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    cnt += 1
                # 공기인 경우 큐에 삽입
                else:
                    queue.append([nx, ny])
                visited[nx][ny] = 1

    return cnt

while True:
    cnt = bfs(0, 0) # 녹은 치즈 개수
    if cnt == 0: break # 더이상 녹을 치즈가 없는 경우 종료
    ans.append(cnt)

print(len(ans))
print(ans[-1])