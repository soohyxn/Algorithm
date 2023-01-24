import heapq

cnt = 1
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북

def dijkstra():
    queue = []
    heapq.heappush(queue, (board[0][0], 0, 0))
    dist[0][0] = board[0][0]

    while queue:
        cur, x, y = heapq.heappop(queue) # 거리, 위치
        # 현재 거리가 최단거리보다 더 길다면 넘어간다
        if cur > dist[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 이동가능한 범위에 있는 경우
                next = cur + board[nx][ny]
                # 다음 거리가 최단거리보다  짧다면 힙에 추가한다
                if next < dist[nx][ny]:
                    heapq.heappush(queue, (next, nx, ny))
                    dist[nx][ny] = next

while True:
    n = int(input())

    if n == 0: # 종료
        break

    board = [list(map(int, input().split())) for _ in range(n)]
    dist = [[1e9] * n for _ in range(n)]

    dijkstra()
    print(f'Problem {cnt}: {dist[n-1][n-1]}')
    cnt += 1