from collections import deque

N = int(input())
no_rg = [list(input()) for _ in range(N)] # 적록색약이 아닌 사람
yes_rg = [[''] * N for _ in range(N)] # 적록색약인 사람
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
ans = [0, 0] # 구역의 수

for i in range(N):
    for j in range(N):
        if no_rg[i][j] == 'B':
            yes_rg[i][j] = 'B'
        else:
            yes_rg[i][j] = 'R' # 적록색약인 사람은 빨강과 초록을 구분하지 못한다

def bfs(i, j, board, target):
    queue = deque([[i, j]])
    board[i][j] = 'X' # 방문 처리

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 아직 방문하지 않았으며 같은 색인 경우
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == target:
                queue.append([nx, ny])
                board[nx][ny] = 'X'

# 구역의 수 구하기
for i in range(N):
    for j in range(N):
        if no_rg[i][j] != 'X':
            bfs(i, j, no_rg, no_rg[i][j])
            ans[0] += 1
        if yes_rg[i][j] != 'X':
            bfs(i, j, yes_rg, yes_rg[i][j])
            ans[1] += 1

print(*ans)