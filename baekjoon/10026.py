from collections import deque

n = int(input())
no_rg = [list(input()) for _ in range(n)] # 적록색약이 아닌 사람이 보는 그림
yes_rg = [[''] * n for _ in range(n)] # 적록색약인 사람이 보는 그림
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
answer = [0, 0] # 구역의 수

# 적록색약인 사람의 그림 구하기
for i in range(n):
    for j in range(n):
        if no_rg[i][j] == 'G': # 적록색약은 빨강과 초록을 구분하지 못한다
            yes_rg[i][j] = 'R'
        else:
            yes_rg[i][j] = no_rg[i][j]

def bfs(a, b, graph, target):
    queue = deque([[a, b]])
    graph[a][b] = 'X'

    while queue:
        x, y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]

            # 그림의 범위를 벗어나면 넘어간다
            if xi < 0 or xi >= n or yi < 0 or yi >= n:
                continue

            # 타켓 색상과 같으면 탐색한다
            if graph[xi][yi] == target:
                queue.append([xi, yi])
                graph[xi][yi] = 'X'

for i in range(n):
    for j in range(n):
        # 적록색약이 아닌 사람의 구역의 수 구하기
        if no_rg[i][j] != 'X':
            bfs(i, j, no_rg, no_rg[i][j])
            answer[0] += 1
        
        # 적록색약인 사람의 구역의 수 구하기
        if yes_rg[i][j] != 'X':
            bfs(i, j, yes_rg, yes_rg[i][j])
            answer[1] += 1

print(*answer)