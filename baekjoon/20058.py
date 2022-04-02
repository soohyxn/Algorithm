import copy
from collections import deque

n, q = map(int, input().split())
N = 2 ** n
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북

for L in list(map(int, input().split())):
    k = 2 ** L # 부분 격자 크기
    # 부분 격자 시계방향 90도 회전
    for x in range(0, N, k):
        for y in range(0, N, k):
            tmp = [board[i][y: y+k] for i in range(x, x+k)]
            for i in range(k):
                for j in range(k):
                    board[x + j][y + k - 1 - i] = tmp[i][j]

    # 얼음 양 감소
    copy_board = copy.deepcopy(board)
    for x in range(N):
        for y in range(N):
            cnt = 0 # 인접한 얼음 수
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and copy_board[nx][ny] > 0:
                    cnt += 1
            if cnt < 3 and copy_board[x][y] > 0: # 인접한 얼음 수가 3 미만인 경우 얼음 감소
                board[x][y] -= 1

print(sum(sum(b) for b in board)) # 남아있는 얼음의 합

# 가장 큰 얼음 덩어리 구하기
visited = [[0] * N for _ in range(N)]
ans = 0 # 가장 큰 얼음 덩어리의 칸 개순
for x in range(N):
    for y in range(N):
        if board[x][y] > 0 and not visited[x][y]:
            queue = deque([[x, y]])
            visited[x][y] = 1
            cnt = 1

            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0 and not visited[nx][ny]:
                        queue.append([nx, ny])
                        visited[nx][ny] = 1
                        cnt += 1
            
            ans = max(ans, cnt)
print(ans)