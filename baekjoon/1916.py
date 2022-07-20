import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
dist = [1e9] * (N+1) # 각 도시의 최단거리

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split()) # 출발점, 도착점

# 최단거리 구하기
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        cost, node = heapq.heappop(heap) # 가장 비용이 적은 노드 가져오기
        # 최단거리를 구한 도시인 경우
        if dist[node] < cost:
            continue
        # 인접한 도시의 최단거리 구하기
        for next in graph[node]:
            next_cost = cost + next[1]
            # 현재 노드를 거치는 경우가 최단거리인 경우
            if next_cost < dist[next[0]]:
                heapq.heappush(heap, (next_cost, next[0]))
                dist[next[0]] = next_cost

dijkstra(start)
print(dist[end])