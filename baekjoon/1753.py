from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = defaultdict(list)
dist = [sys.maxsize for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    queue = []
    dist[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        cur_dist, node = heapq.heappop(queue)
        if cur_dist > dist[node]:
            continue
        for adj_node, adj_dist in graph[node]:
            cost = cur_dist + adj_dist
            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heapq.heappush(queue, (cost, adj_node))

dijkstra(start)
for i in range(1, V+1):
    if dist[i] == sys.maxsize:
        print('INF')
    else:
        print(dist[i])