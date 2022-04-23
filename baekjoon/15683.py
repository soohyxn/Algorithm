import copy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
cctv = [] # cctv 리스트
dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
} # cctv 종류에 따른 감시 방향
ans = 1e9 # 최소 사각지대 크기

# cctv 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv.append([i, j, board[i][j]]) # x위치, y위치, cctv 종류

def watch(x, y, dir, tmp):
    for d in dir:
        nx, ny = x, y
        # 이동할 수 없을 때까지 이동하면서 '#'으로 변경
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or tmp[nx][ny] == 6: # 이동 가능한 범위를 벗어나거나 벽인 경우
                break
            if tmp[nx][ny] == 0: # 빈칸이면 감시 구역으로 변경
                tmp[nx][ny] = '#'

def dfs(n, board):
    global ans

    if n == len(cctv):
        count = sum([b.count(0) for b in board]) # 사각지대 크기
        ans = min(ans, count)
        return

    x, y, c = cctv[n]
    tmp = copy.deepcopy(board)
    # 해당 cctv의 종류에 따른 감시 구역을 구한다
    for dir in dirs[c]:
        watch(x, y, dir, tmp)
        dfs(n+1, tmp)
        tmp = copy.deepcopy(board)

dfs(0, board)
print(ans)