N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0] # 서남동북
ans = 0 # 격자 밖으로 나간 모래의 양

# 방향에 따른 모래 비율 위치
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1), (-1, -1, 0.1), 
        (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
dict = {0: left, 1: down, 2: right, 3: up}

# 모래 흩날리기
def scatter(x, y, dir):
    global ans
    total = 0 # 비율이 적혀있는 칸으로 이동하는 모래의 양

    for dx, dy, z in dir:
        nx = x + dx
        ny = y + dy
        # 이동할 모래의 양을 구한다
        if z == 0:
            new = a[x][y] - total # 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양
        else:
            new = int(a[x][y] * z) # 해당 비율의 모래의 양
            total += new

        # 모래 이동
        if 0 <= nx < N and 0 <= ny < N: # 범위 내에 있는 경우 기존 모래에 누적
            a[nx][ny] += new
        else: # 범위를 벗어나는 경우 ans에 누적
            ans += new

x, y = N//2, N//2 # 가운데 칸 위치
time = 0 # 반복 횟수
for i in range(2*N-1):
    d = i % 4 # 이동 방향
    if d == 0 or d == 2:
        time += 1
    
    # 반복 횟수만큼 모래 흩날리기
    for _ in range(time):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            scatter(nx, ny, dict[d])
        x, y = nx, ny

print(ans)