from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], [] # 집과 치킨집 위치
ans = 1e9 # 도시의 치킨거리 최소값

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])

for com in combinations(chicken, m):
    dist = [1e9] * len(house) # 각 집의 치킨거리
    for i, h in enumerate(house):
        for c in com:
            dist[i] = min(dist[i], abs(h[0] - c[0]) + abs(h[1] - c[1]))
    ans = min(ans, sum(dist))

print(ans)