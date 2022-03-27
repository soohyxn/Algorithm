n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9 # 인구 차이 최소값

def solve(x, y, d1, d2):
    board = [[0] * n for _ in range(n)] # 각 위치이 선거구
    cnt = [0] * 6 # 선거구별 인구수

    # 경계선 - 5번 선거구
    for i in range(d1 + 1):
        board[x + i][y - i] = 5
        board[x + d2 + i][y + d2 - i] = 5

    for i in range(d2 + 1):
        board[x + i][y + i] = 5
        board[x + d1 + i][y - d1 + i] = 5
    
    # 경계선 안쪽 - 5번 선거구
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(n):
            if board[i][j] == 5: flag = not flag
            if flag: board[i][j] = 5

    # 선거구별 인구수 세기
    for r in range(n):
        for c in range(n):
            if r < x + d1 and c <= y and board[r][c] == 0: # 1번 선거구
                cnt[1] += people[r][c]
            elif r <= x + d2 and y < c and board[r][c] == 0: # 2번 선거구
                cnt[2] += people[r][c]
            elif x + d1 <= r and c < y - d1 + d2 and board[r][c] == 0: # 3번 선거구
                cnt[3] += people[r][c]
            elif x + d2 < r and y - d1 + d2 <= c and board[r][c] == 0: # 4번 선거구
                cnt[4] += people[r][c]
            elif board[r][c] == 5: # 5번 선거구
                cnt[5] += people[r][c]
    
    return max(cnt[1:]) - min(cnt[1:])

for x in range(n):
    for y in range(n):
        for d1 in range(1, n-1):
            for d2 in range(1, n-1):
                if 0 <= x < x + d1 + d2 <= n-1 and 0 <= y - d1 < y < y + d2 <= n-1:
                    result = solve(x, y, d1, d2) # 선거구 나누기
                    ans = min(ans, result)

print(ans)