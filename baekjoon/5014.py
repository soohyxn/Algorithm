from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0] * (f+1)

def bfs(start):
    queue = deque([[start, 0]])
    visited[start] = 1

    while queue:
        v, cnt = queue.popleft() # 현재 위치, 누른 버튼 수

        # G층에 도착하면 종료
        if v == g:
            return cnt
        
        # 위로 U층 이동할 수 있는 경우
        if v + u <= f and not visited[v + u]:
            queue.append([v + u, cnt + 1])
            visited[v + u] = 1
        
        # 아래로 D층 이동할 수 있는 경우
        if v - d >= 1 and not visited[v - d]:
            queue.append([v - d, cnt + 1])
            visited[v - d] = 1
    
    # 엘리베이터로 이동할 수 없는 경우
    return 'use the stairs'

print(bfs(s))