from collections import deque
import heapq

n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tx, ty = map(int, input().split())
taxi, start, end = [tx-1, ty-1], [], [] # 현재 택시 위치, 승객의 출발지/도착지 리스트
check = [0] * m # 승객을 목적지로 이동시켰는지 확인 리스트
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북

for _ in range(m):
    sx, sy, ex, ey = map(int, input().split())
    start.append([sx-1, sy-1])
    end.append([ex-1, ey-1])

# 출발지에서 목적지까지 최단거리 구하기
def bfs():
    queue = deque([taxi])
    visited = [[0] * n for _ in range(n)] # 방문 여부 리스트
    dist = [[1e9] * n for _ in range(n)] # 최단 거리 리스트
    # 출발지 초기화
    visited[taxi[0]][taxi[1]] = 1
    dist[taxi[0]][taxi[1]] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위이며 아직 방문하지 않았고 빈칸인 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1

    return dist

# 택시에 태울 승객 고르기
def find_passenger():
    global fuel
    heap = []
    dist = bfs()

    for i in range(m):
        if not check[i]:
            x, y = start[i] # 출발지 위치
            d = dist[x][y] # 출발지까지 최단거리
            if fuel - d >= 0:
                heapq.heappush(heap, [d, x, y, i]) # 우선순위: 거리 -> 행 -> 열

    # 태울 수 있는 승객이 없는 경우
    if not heap:
        return -1

    d, _, _, i = heapq.heappop(heap) # 현재 택시 위치에서 최단거리가 가장 짧은 승객
    fuel -= d # 연료 감소
    check[i] = 1

    return i

# 승객을 목적지까지 이동시키기
def go_destination(p_idx):
    global fuel
    dist = bfs()
    x, y = end[p_idx] # 목적지 위치
    d = dist[x][y] # 목적지까지 최단거리

    if fuel - d >= 0: # 목적지까지 이동시킬 수 있는 경우
        return d
    else: # 그렇지 않은 경우
        return -1

flag = True # 모든 승객을 이동시킬 수 있는지
cnt = m # 이동 시킬 승객 수
while cnt:
    p_idx = find_passenger() # 택시에 태울 승객 고르기

    if p_idx == -1: # 태울 수 있는 승객이 없는 경우
        flag = False
        break

    taxi = start[p_idx] # 택시 위치를 승객의 출발지로
    d = go_destination(p_idx) # 출발지부터 목적지까지 최단거리 구하기
    
    if d == -1: # 목적지까지 이동시킬 수 없는 경우
        flag = False
        break

    fuel += d # 연료 충전
    taxi = end[p_idx] # 택시 위치를 승객의 목적지로
    cnt -= 1

print(fuel) if flag else print(-1)