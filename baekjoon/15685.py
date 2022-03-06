n = int(input())
board = [[0] * 101 for _ in range(101)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 동북서남
answer = 0 # 드래곤 커브 일부인 것의 개수

for _ in range(n):
    y, x, d, g = map(int, input().split()) # 시작점, 시작방향, 세대
    board[x][y] = 1

    # 커브 리스트 구하기
    curve = [d]
    for i in range(g):
        for j in range(len(curve)-1, -1, -1):
            curve.append((curve[j] + 1) % 4)

    # 드래곤 커브 만들기
    for c in curve:
        x += dx[c]
        y += dy[c]
        if x < 0 or x > 100 or y < 0 or y > 100:
            continue
        board[x][y] = 1

# 드래곤 커브 일부인 것의 개수 구하기
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            answer += 1

print(answer)