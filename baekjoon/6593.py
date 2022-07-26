from collections import deque

def bfs(i, j, k):
    queue = deque([[i, j, k]])
    visited[i][j][k] = 1

    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위이며 아직 방문하지 않은 경우
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and not visited[nz][nx][ny]:
                # 출구일 경우 최단 시간 리턴
                if board[nz][nx][ny] == 'E':
                    return visited[z][x][y]
                # 빈칸일 경우 이동
                elif board[nz][nx][ny] == '.':
                    queue.append([nz, nx, ny])
                    visited[nz][nx][ny] = visited[z][x][y] + 1
    
    return -1 # 탈출이 불가능하다면 -1 리턴


while True:
    L, R, C = map(int, input().split())

    # 입력의 끝이라면 종료
    if L == 0 and R == 0 and C == 0: break

    board = [[] for _ in range(L)]
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    # 동서남북상하
    dx = [0, 0, 1, -1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for i in range(L):
        for j in range(R):
            board[i].append(list(input()))
        input()

    for i in range(L):
        for j in range(R):
            for k in range(C):
                # 시작 지점인 경우 최단 시간을 구한다
                if board[i][j][k] == 'S':
                    result = bfs(i, j, k)
                    if result == -1:
                        print("Trapped!")
                    else:
                        print(f'Escaped in {result} minute(s).')
                        break