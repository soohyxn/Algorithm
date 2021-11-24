from collections import deque

N, K = map(int, input().split())
dist = [0] * 100001

def bfs(n):
    queue = deque([[n, 0]])
    dist[n] = 1

    while queue:
        x, time = queue.popleft()
        if x == K:
            return time

        if x > 0 and not dist[x-1]:
            queue.append([x - 1, time + 1])
            dist[x-1] = 1
        if x < 100000 and not dist[x+1]:
            queue.append([x + 1, time + 1])
            dist[x+1] = 1
        if x < 50001 and not dist[x*2] and abs(x*2-K) < abs(x-K):
            queue.append([x * 2, time + 1])
            dist[x*2] = 1

answer = bfs(N)
print(answer)