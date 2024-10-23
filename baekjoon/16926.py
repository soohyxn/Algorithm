from collections import deque

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
deq = deque()
answer = [[0] * m for _ in range(n)]

for i in range(min(n, m) // 2):
    # 초기화
    deq.clear()

    # 2차원 배열 -> 1차원 배열로 변환
    deq.extend(board[i][i:m-i]) # 위쪽
    deq.extend(row[m-i-1] for row in board[i+1:n-i-1]) # 오른쪽 
    deq.extend(board[n-i-1][i:m-i][::-1]) # 아래쪽
    deq.extend(row[i] for row in board[i+1:n-i-1][::-1]) # 왼쪽

    # 1차원 배열 반시계 방향으로 회전
    deq.rotate(-r)

    # 1차원 배열 -> 2차원 배열로 변환 
    for j in range(i, m-i): # 위쪽
        answer[i][j] = deq.popleft()
    for j in range(i+1, n-i-1): # 오른쪽
        answer[j][m-i-1] = deq.popleft()
    for j in range(m-i-1, i-1, -1): # 아래쪽
        answer[n-i-1][j] = deq.popleft()
    for j in range(n-i-2, i, -1): # 왼쪽
        answer[j][i] = deq.popleft()

for row in answer:
    print(*row)