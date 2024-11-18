from collections import deque

def bfs(start, visited, board):
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        v = queue.popleft()
        
        # 다음 지역 탐색
        for next in board[v]:
            # 아직 방문하지 않은 지역이면 방문한다
            if visited[next] < 0:
                queue.append(next)
                visited[next] = visited[v] + 1

def solution(n, roads, sources, destination):
    answer = []
    board = [[] for _ in range(n+1)]
    visited = visited = [-1] * (n+1) # 최단시간 리스트
    
    for x, y in roads:
        board[x].append(y)
        board[y].append(x)
    
    # 부대로 복귀하는 최단시간 구하기
    bfs(destination, visited, board)
    
    for source in sources:
        answer.append(visited[source])
    
    return answer