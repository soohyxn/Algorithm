from collections import deque

N, M = map(int, input().split())
snakes, ladders = {}, {}
dist = [0] * 101 # 각 위치의 주사위를 굴리는 최소 횟수

for _ in range(N):
    x, y = map(int, input().split())
    snakes[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    ladders[u] = v

def bfs(start):
    queue = deque([start])
    visited = [0] * 101
    visited[1] = 1

    while queue:
        now = queue.popleft() # 현재 위치
        # 주사위를 굴린다
        for num in range(1, 7):
            move = now + num # 이동 위치
            if 1 <= move <= 100 and not visited[move]:
                # 뱀이 있는 칸인 경우
                if move in snakes.keys():
                    move = snakes[move]
                
                # 사다리가 있는 칸인 경우
                if move in ladders.keys():
                    move = ladders[move]

                # 아직 방문하지 않았다면 이동
                if not visited[move]:
                    queue.append(move)
                    visited[move] = 1
                    dist[move] = dist[now] + 1

bfs(1)
print(dist[100])