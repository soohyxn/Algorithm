from itertools import combinations
from collections import deque
import copy

N = int(input())
board = [list(input().split()) for _ in range(N)]
blank, teacher = [], []
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
flag = False # 감시를 피할 수 있는지 여부

for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            blank.append([i, j])
        elif board[i][j] == 'T':
            teacher.append([i, j])

def bfs(copy_board):
    queue = deque(teacher)

    while queue:
        tx, ty = queue.popleft() # 선생님 위치
        # 4방향을 감시한다
        for i in range(4):
            x, y = tx, ty
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    # 빈칸인 경우 -> 방문 표시
                    if copy_board[nx][ny] == 'X':
                        copy_board[nx][ny] = 'T'
                    # 학생인 경우 -> 감시를 피하지 못한다
                    elif copy_board[nx][ny] == 'S':
                        return False
                    # 장애물인 경우 -> 감시를 피한다
                    elif copy_board[nx][ny] == 'O':
                        break
                    x, y = nx, ny
                else:
                    break
    
    return True

# 완전탐색
for com in combinations(blank, 3):
    copy_board = copy.deepcopy(board)

    # 장애물 3개 설치
    for i, j in com:
        copy_board[i][j] = 'O'

    # 감시를 피할 수 있는지 체크
    if bfs(copy_board):
        flag = True
        break

print('YES' if flag else 'NO')