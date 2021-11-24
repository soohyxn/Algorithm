t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    answer = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    def bfs(i, j):
        queue = [[i, j]]
        graph[i][j] = 0

        while queue:
            x, y = queue.pop(0)
            for i in range(4):
                xi = x + dx[i]
                yi = y + dy[i]
                if xi <= -1 or xi >= n or yi <= -1 or yi >= m:
                    continue
                if graph[xi][yi] == 1:
                    queue.append([xi, yi])
                    graph[xi][yi] = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                answer += 1

    print(answer)