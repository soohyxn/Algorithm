from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북

def bfs(place, people):
    for i, j in people:
        queue = deque([[i, j]])
        visited = [[-1] * 5 for _ in range(5)]
        visited[i][j] = 0
        
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == -1: # 이동 가능한 범위이며 아직 방문하지 않는 경우
                    if place[nx][ny] == 'O': # 빈 테이블인 경우
                        queue.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1
                        
                    if place[nx][ny] == 'P' and visited[x][y] <= 1: # 대기실이며 거리가 2이하인 경우
                        return 0
                    
    return 1        

def solution(places):
    answer = []
    
    for place in places:
        people = [] # 대기실 리스트
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append([i, j])
                    
        result = bfs(place, people)
        answer.append(result)
        
    return answer