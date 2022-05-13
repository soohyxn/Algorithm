import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [1e9] * (N+1) # 헛간별 최단 경로

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dijkstra(start):
    queue = []
    # 시작 노드는 큐에 삽입하고 최단 경로는 0으로 설정
    heapq.heappush(queue, (0, start))
    dist[start] = 0

    while queue:
        d, node = heapq.heappop(queue) # 거리, 현재 노드
        
        # 현재 노드가 이미 처리된 적이 있다면 무시
        if dist[node] < d:
            continue

        # 현재 노드와 인접한 노드들 확인
        for i in graph[node]:
            cost = d + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 빠른 경우
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(1)
print(dist[N])