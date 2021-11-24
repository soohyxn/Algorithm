n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
answer = []
count = result = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            answer.append(count)
            result += 1
            count = 0

answer.sort()
print(result)
print(*answer)     