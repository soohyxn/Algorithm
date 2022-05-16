from collections import deque

def bfs(start, n, computers, visited):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        node = queue.popleft()
        for next in range(n):
            # 자기 자신이 아니고 아직 방문하지 않았으며 연결된 경우
            if node != next and not visited[next] and computers[node][next]:
                queue.append(next)
                visited[next] = 1
    
def solution(n, computers):
    answer = 0
    visited = [0] * n

    for node in range(n):
        if not visited[node]:
            bfs(node, n, computers, visited)
            answer += 1
    
    return answer