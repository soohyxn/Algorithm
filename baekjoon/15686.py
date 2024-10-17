from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], [] # 집 위치, 치킨집 위치
answer = 1e9 # 최소 도시의 치킨 거리

# 집과 치킨집 위치 구하기
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])

# 가장 수익을 많이 낼 모든 치킨집 경우 탐색
for com in combinations(chicken, m):
    city_dist = [] # 도시의 치킨 거리 (= 모든 집의 치킨 거리의 합)
    # 집의 치킨 거리 구하기
    for hx, hy in house:
        house_dist = 1e9 # 최소 집의 치킨 거리
        for cx, cy in com:
            house_dist = min(house_dist, abs(cx - hx) + abs(cy - hy))
        city_dist.append(house_dist)
    answer = min(answer, sum(city_dist))    

print(answer)