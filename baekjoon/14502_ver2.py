from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
blank, virus = [], [] # 빈칸, 바이러스 위치 리스트
ans = 0 # 안전영역 크기의 최대값

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            blank.append([i, j])
        elif board[i][j] == 2:
            virus.append([i, j])

for com in combinations(blank, 3):
    cb = copy.deepcopy(board)
    queue = deque(virus) # 바이러스 위치를 큐에 삽입

    # 벽 세우기
    for x, y in com:
        cb[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and cb[nx][ny] == 0:
                cb[nx][ny] = 2
                queue.append([nx, ny])

    count = sum([b.count(0) for b in cb])
    ans = max(ans, count) # 안전영역 크기의 최대값을 구한다

print(ans)