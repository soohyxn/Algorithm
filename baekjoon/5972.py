import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [1e9] * (N+1) # 각 헛간의 최소 여물 비용

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 1))
    dist[1] = 0

    # 최소 비용을 구한다
    while queue:
        cost, node = heapq.heappop(queue) # 비용, 헛간 번호

        # 최소 비용보다 현재 비용이 크다면 넘어간다
        if dist[node] < cost:
            continue

        # 연결된 모든 헛간 탐색
        for x, y in graph[node]:
            new_cost = cost + y
            # 새로운 비용이 최소 비용보다 작다면 갱신한다
            if new_cost < dist[x]:
                heapq.heappush(queue, (new_cost, x))
                dist[x] = new_cost

dijkstra()
print(dist[N])