n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0] # 동서북남
dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for dir in move:
    # 이동할 위치
    nx = x + dx[dir-1]
    ny = y + dy[dir-1]

    # 이동 범위를 벗어나면 무시한다
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    # 이동 방향에 따른 주사위 재배치
    if dir == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif dir == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif dir == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif dir == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    
    # 이동할 칸에 쓰여 있는 수에 따른 처리
    if board[nx][ny] == 0:
        board[nx][ny] = dice[6]
    else:
        dice[6] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny
    print(dice[1]) # 주사위 상단 값 출력