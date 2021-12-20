from collections import deque

N = int(input())
K = int(input())
graph = [[0] * N for _ in range(N)] #
# 사과 위치는 1로
for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
L = int(input())
times = {} 
for _ in range(L):
    x, c = input().split()
    times[int(x)] = c

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북, 동, 남, 서
direction = 1 # 초기 방향 - 동쪽
time = 1 # 시간
x, y = 0, 0 # 초기 위치
visited = deque([[x, y]]) # 방문 위치
graph[x][y] = 2 # 뱀의 위치는 2로

while True:
    x, y = x + dx[direction], y + dy[direction] # 이동할 머리 위치
    if x < 0 or x >= N or y < 0 or y >= N or graph[x][y] == 2: # 이동할 수 없거나 자기 자신과 부딛히는 경우 게임을 끝낸다
        break
    else:
        if graph[x][y] == 0: # 이동할 위치가 사과라면 꼬리 제거
            vx, vy = visited.popleft()
            graph[vx][vy] = 0
        graph[x][y] = 2 # 머리 위치를 2로
        visited.append([x, y])
        if time in times.keys(): # 방향을 바꿀 시간이면 방향을 바꾼다
            if times[time] == 'L':
                direction = (direction + 3) % 4
            else:
                direction = (direction + 1) % 4
        time += 1

print(time)