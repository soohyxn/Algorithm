def solution(grid):
    answer = []
    n, m = len(grid), len(grid[0]) # 세로길이, 가로길이
    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)] # 방향, 위치별 방문 확인 리스트
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 남서북동
    
    # 완전탐색
    for x in range(n):
        for y in range(m):
            for d in range(4):
                # 헤당 방향의 위치를 방문한 경우
                if visited[x][y][d]:
                    continue
                    
                cnt = 0 # 사이클의 길이
                nx, ny, nd = x, y, d
                
                while True:
                    visited[nx][ny][nd] = 1
                    cnt += 1
                    
                    # 방향 변경
                    if grid[nx][ny] == 'L':
                        nd = (nd - 1) % 4
                    elif grid[nx][ny] == 'R':
                        nd = (nd + 1) % 4
                        
                    # 위치 변경
                    nx = (nx + dx[nd]) % n
                    ny = (ny + dy[nd]) % m
                    
                    # 출발점에 도착하였다면 사이클 완성
                    if nx == x and ny == y and nd == d:
                        break
                
                answer.append(cnt)
    
    answer.sort()
    return answer