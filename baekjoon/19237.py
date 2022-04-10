import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dir = list(map(int, input().split()))
prior = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 북남서동
shark = [[] for _ in range(m)]

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            shark[board[i][j]-1] = [i, j, dir[board[i][j]-1]-1]
            board[i][j] = [board[i][j]-1, k]

ans = 0
while ans <= 1000:
    ans += 1

    check = [[0] * n for _ in range(n)]
    for i in range(m):
        if shark[i] != 0:
            x, y, d = shark[i]
            flag = 0

            for j in range(4):
                ndir = prior[i][d][j] - 1
                nx = x + dx[ndir]
                ny = y + dy[ndir]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    flag = 1
                    break
            
            if flag == 0:
                for j in range(4):
                    ndir = prior[i][d][j] - 1
                    nx = x + dx[ndir]
                    ny = y + dy[ndir]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny][0] == i:
                        break

            if check[nx][ny]:
                if check[nx][ny] < i:
                    shark[i] = 0
                else:
                    shark[check[nx][ny]] = 0

            else:
                check[nx][ny] = i
                shark[i] = [nx, ny, ndir]

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j] = 0

    for i in range(m):
        if shark[i] != 0:
            x, y, d = shark[i]
            board[x][y] = [i, k]
    
    if shark.count(0) == m-1:
        print(ans)
        exit()

print(-1)