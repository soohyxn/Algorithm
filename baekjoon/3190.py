from collections import deque

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1 # 사과 위치는 1로

L = int(input())
turn = {}

for _ in range(L):
    t, d = input().split()
    turn[int(t)] = d

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
x, y, dir = 0, 0, 0 # 시작 위치, 방향(동쪽)
snake = deque([[x, y]]) # 뱀의 위치
board[x][y] = 2 # 뱀의 위치는 2로
ans = 1 # 게임 시간

while True:
    # 이동할 머리 위치
    x = x + dx[dir]
    y = y + dy[dir]

    if x < 0 or x >= N or y < 0 or y >= N or board[x][y] == 2: # 벽이거나 자기 자신과 부딛히는 경우 게임 종료
        break

    if board[x][y] == 0: # 이동한 칸에 사과가 없다면 꼬리 제거
        tx, ty = snake.popleft()
        board[tx][ty] = 0
    # 머리 이동
    board[x][y] = 2
    snake.append([x, y])

    # 방향을 바꿀 시간이면 방향을 바꾼다
    if ans in turn.keys():
        if turn[ans] == 'L':
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4

    ans += 1

print(ans)