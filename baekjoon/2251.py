from collections import deque

a, b, c = map(int, input().split())
ans = []

queue = deque([[0, 0]])
visited = [[0] * (b+1) for _ in range(a+1)]
visited[0][0] = 1

# 경우의 수 저장
def pour(x, y):
    if not visited[x][y]:
        queue.append([x, y])
        visited[x][y] = 1

def bfs():
    while queue:
        x, y = queue.popleft() # A물통 물의 양, B물통 물의 양
        z = c - x - y # C물통 물의 양

        # A물통이 비었다면 C물통에 남아있는 물의 양 저장
        if x == 0: ans.append(z)

        # A물통 -> B물통
        water = min(x, b-y)
        pour(x - water, y + water)
        # A물통 -> C물통
        water = min(x, c-z)
        pour(x - water, y)
        # B물통 -> A물통
        water = min(y, a-x)
        pour(x + water, y - water)
        # B물통 -> C물통
        water = min(y, c-z)
        pour(x, y - water)
        # C물통 -> A물통
        water = min(z, a-x)
        pour(x + water, y)
        # C물통 -> B물통
        water = min(z, b-y)
        pour(x, y + water)

bfs()
ans.sort()
print(*ans)