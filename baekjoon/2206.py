from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0] # 동서남북

def bfs(i, j):
    queue = deque([[i, j, 0]])
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)] # 방문 확인 리스트
    visited[i][j][0] = 1 # 시작점 벽을 안 부순 상태로 시작

    while queue:
        x, y, w = queue.popleft()
        if x == n-1 and y == m-1: # 이동하려는 위치에 도착하면 최단경로 리턴
            return visited[x][y][w]
        for i in range(4):
            # 다음에 이동할 위치
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][w] == 0: # 이동 가능하며 아직 방문하지 않은 경우
                if graph[nx][ny] == 0: # 벽이 아니라면 이동
                    queue.append([nx, ny, w])
                    visited[nx][ny][w] = visited[x][y][w] + 1
                elif graph[nx][ny] == 1 and w == 0: # 벽이고 벽을 안 부순 상태라면 벽을 부수고 이동
                    queue.append([nx, ny, 1])
                    visited[nx][ny][1] = visited[x][y][w] + 1
    return -1 # 이동하려는 위치에 도달하지 못하는 경우 -1 리턴

print(bfs(0, 0))