from collections import deque

r, c, n = map(int, input().split())
graph = [list(input()) for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find_bombs():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                queue.append([i, j])

def make_bombs():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = 'O'

def explode():
    while queue:
        x, y = queue.popleft()
        graph[x][y] = '.'
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if xi <= -1 or xi >= r or yi <= -1 or yi >= c:
                continue
            graph[xi][yi] = '.'

n -= 1
while n:
    queue = deque()
    find_bombs()
    make_bombs()
    n -= 1
    if n < 0:
        break
    explode()
    n -= 1

for i in range(r):
    for j in range(c):
        print(graph[i][j], end='')
    print()