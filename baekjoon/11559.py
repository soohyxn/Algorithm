from collections import deque
import sys
input = sys.stdin.readline

board = [list(input()) for _ in range(12)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
ans = 0 # 연쇄 횟수

# 뿌요 없애기
def bfs(i, j, color):
    queue = deque([[i, j]])
    visited[i][j] = 1
    puyo = [[i, j]] # 같은색의 뿌요 리스트

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위에 있으며 아직 방문하지 않았고 같은색의 뿌요인 경우
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and board[nx][ny] == color:
                queue.append([nx, ny])
                visited[nx][ny] = 1
                puyo.append([nx, ny])

    # 같은색의 뿌요가 4개 이상이면 없어진다
    if len(puyo) >= 4:
        for x, y in puyo:
            board[x][y] = '.'
        return True
    else:
        return False

# 뿌요 아래로 떨어지기
def down():
    for j in range(6):
        queue = deque() # 뿌요 리스트
        # 뿌요를 리스트에 저장한다
        for i in range(11, -1, -1):
            if board[i][j] != '.':
                queue.append(board[i][j])
        # 뿌요를 아래로 옮기고 나머지는 빈칸으로 채운다
        for i in range(11, -1, -1):
            if queue:
                board[i][j] = queue.popleft()
            else:
                board[i][j] = '.'

while True:
    visited = [[0] * 6 for _ in range(12)]
    flag = False # 뿌요가 있는지 체크

    for i in range(12):
        for j in range(6):
            if not visited[i][j] and board[i][j] != '.':
                if bfs(i, j, board[i][j]):
                    flag = True 

    # 터트릴 뿌요가 없는 경우 종료
    if not flag: break

    ans += 1
    down()

print(ans)