r1, c1, r2, c2 = map(int, input().split())
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 동북서남
board = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
n = (r2-r1+1) * (c2-c1+1) # 출력할 숫자 개수

x, y, d = 0, 0, 0 # 시작 위치, 방향
num, max_len = 1, 0 # 현재 숫자, 숫자 최대 길이
cnt, dcnt = 0, 1 # 현재 방향에서 출력한 숫자 개수, 방향에 따른 출력할 숫자 개수

while n > 0:
    # 출력할 범위 내에 있다면 숫자를 출력
    if r1 <= x <= r2 and c1 <= y <= c2:
        n -= 1
        board[x - r1][y - c1] = num
        max_len = max(max_len, len(str(num)))

    # 다음 위치로 이동
    num += 1
    cnt += 1
    x = x + dx[d]
    y = y + dy[d]

    # 방향에 따른 정보 갱신
    if cnt == dcnt:
        cnt = 0
        d = (d + 1) % 4
        if d == 0 or d == 2: dcnt += 1

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(' ' * (max_len - len(str(board[i][j]))) + str(board[i][j]), end = ' ') # 숫자 최대 길이에 맞춰 숫자 출력
    print()