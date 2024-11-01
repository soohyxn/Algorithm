from collections import deque

n, m = map(int, input().split())
ladder, snake = {}, {} # 사다리와 뱀의 위치
dist = [-1] * 101 # 주사위를 굴리는 최소값 리스트

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

def bfs(start):
    queue = deque([start])
    dist[start] = 0

    while queue:
        cur = queue.popleft()

        # 주사위를 굴린다
        for i in range(1, 7):
            next = cur + i

            # 보드판 범위를 벗어나거나 이미 방문한 경우 넘어간다
            if next < 1 or next > 100 or dist[next] >= 0:
                continue

            if next in ladder:
                next = ladder[next]
            
            if next in snake:
                next = snake[next]
            
            # 아직 방문하지 않은 경우 사다리 or 뱀을 통해 이동한다
            if dist[next] < 0:
                queue.append(next)
                dist[next] = dist[cur] + 1

bfs(1)
print(dist[100])