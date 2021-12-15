from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

def bfs(start):
    queue = deque([start])
    visited = [0] * (N+1)
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

    return visited.count(1)

max = 0
answer = []
for i in range(1, N+1):
    count = bfs(i)
    if count > max:
        max = count
    answer.append([i, count])

for i, count in answer:
    if count == max:
        print(i, end=' ')