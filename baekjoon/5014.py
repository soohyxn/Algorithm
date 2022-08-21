from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)

def bfs(start):
    queue = deque([[start, 0]])
    visited[start] = 1

    while queue:
        x, cnt = queue.popleft() # 현재 층수, 누른 버튼수

        # 스타트링크 위치(G층)인 경우
        if x == G:
            return cnt

        # 위로 U층 이동
        if x + U <= F and not visited[x + U]:
            queue.append([x + U, cnt + 1])
            visited[x + U] = 1

        # 아래로 D층 이동
        if x - D >= 1 and not visited[x - D]:
            queue.append([x - D, cnt + 1])
            visited[x - D] = 1

    # 엘리베이터로 이동 불가능한 경우
    return 'use the stairs'

print(bfs(S))