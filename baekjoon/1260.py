from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 정점번호가 작은순으로 방문하도록 정렬
for g in graph:
    g.sort()

def dfs(node):
    visited_dfs[node] = 1
    print(node, end=' ')

    # 다음 정점 탐색
    for next in graph[node]:
        if not visited_dfs[next]:
            dfs(next)

def bfs(start):
    queue = deque([start])
    visited_bfs[start] = 1

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        # 다음 정점 탐색
        for next in graph[node]:
            if not visited_bfs[next]:
                queue.append(next)
                visited_bfs[next] = 1

dfs(v)
print()
bfs(v)