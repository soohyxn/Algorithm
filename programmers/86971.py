from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = 1
    cnt = 1
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                cnt += 1
    
    return cnt

def solution(n, wires):
    answer = 1e9 # 두 전력망이 가지고 있는 송전탑 개수의 차이의 최소값
    graph = [[] for _ in range(n+1)]
    
    # 연결 관계 구하기
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    # 연결 관계를 하나씩 삭제해보면서 최소 개수 차이 구하기
    for start, delete in wires:
        visited = [0] * (n+1)
        visited[delete] = 1 # 연결이 끊긴 노드는 방문 처리
        result = bfs(start, graph, visited)
        answer = min(answer, abs(result - (n - result)))

    return answer