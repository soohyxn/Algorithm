import heapq, sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
dist = [1e9] * (V+1) # 각 노드의 최단거리

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def dijkstra(start):
    queue = []
    heapq.heappush(queue, [0, start])
    dist[start] = 0 # 시작 노드

    while queue:
        d, node = heapq.heappop(queue)
        # 현재 노드가 이미 처리된 경우
        if dist[node] < d:
            continue
        # 인접한 노드 확인
        for i in graph[node]:
            cost = d + i[1]
            # 현재 노드를 거쳐가는 경우가 최단거리인 경우
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(queue, [cost, i[0]])

dijkstra(K)
for i in range(1, V+1):
    print(dist[i] if dist[i] != 1e9 else 'INF')