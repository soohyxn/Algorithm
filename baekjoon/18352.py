import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)

distance = [-1] * (n+1)
queue = deque([x])
distance[x] = 0

while queue:
	v = queue.popleft()

	for i in graph[v]:
		if distance[i] == -1:
			queue.append(i)
			distance[i] = distance[v] + 1

city = False
for i in range(1, n+1):
	if distance[i] == k:
		print(i)
		city = True

if city == False:
	print(-1)
