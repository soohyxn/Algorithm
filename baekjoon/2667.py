n = int(input())
board = [list(map(int, input())) for _ in range(n)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 동남서북
count = 0 # 집의 수
answer = []

def dfs(x, y):
    # 지도의 범위를 벗어나면 넘어간다
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    # 집이 있는 곳이면 방문한다
    if board[x][y] == 1:
        global count
        count += 1
        board[x][y] = -1 # 방문 처리
        # 4방향 탐색
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    
    return False

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            if dfs(i, j):
                answer.append(count)
                count = 0

answer.sort()
print(len(answer))
print(*answer)