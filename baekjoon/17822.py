from collections import deque

n, m, t = map(int, input().split())
board = [deque(list(map(int, input().split()))) for _ in range(n)]

for _ in range(t):
    x, d, k = map(int, input().split())

    # [조건 1] 원판 회전하기
    for i in range(n):
        if (i+1) % x == 0:
            if d == 0: # 시계 방향
                board[i].rotate(k)
            else: # 반시계 방향
                board[i].rotate(-k)

    # [조건 2] 인접한 수 찾기
    remove = set() # 제거할 수의 위치
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and board[i][(j+1) % m] > 0 and board[i][j] == board[i][(j+1) % m]: # 같은 원 내에서
                remove.add((i, j))
                remove.add((i, (j+1) % m))
            if i < n-1 and board[i][j] > 0 and board[i+1][j] > 0 and board[i][j] == board[i+1][j]: # 다른 원에서
                remove.add((i, j))
                remove.add((i+1, j))
    
    # [조건 2-1] 수 제거하기
    for i, j in remove:
        board[i][j] = 0

    # [조건 2-2] 수 변경하기
    if len(remove) == 0:
        all, zero = 0, 0

        # 원판 평균 구하기
        for b in board:
            all += sum(b)
            zero += b.count(0)
        cnt = n * m - zero
        if cnt > 0: avg = all / cnt

        # 수 변경
        for i in range(n):
            for j in range(m):
                if board[i][j] > 0:
                    if board[i][j] > avg:
                        board[i][j] -= 1
                    elif board[i][j] < avg:
                        board[i][j] += 1

print(sum([sum(b) for b in board]))