from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북

def bfs(n, m, maps):
    queue = deque([[0, 0]])
    dist = [[-1] * m for _ in range(n)] # 최단거리
    dist[0][0] = 1 # 시작지점
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위에 있으며 벽이 아니고 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and dist[nx][ny] == -1:
                queue.append([nx, ny])
                dist[nx][ny] = dist[x][y] + 1 # 최단거리 갱신

    return dist[n-1][m-1] # 도착지점
    
def solution(maps):
    n = len(maps) # 행의 길이
    m = len(maps[0]) # 열의 길이
    
    answer = bfs(n, m, maps)
    return answer