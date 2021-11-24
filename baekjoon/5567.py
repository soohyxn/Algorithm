n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

def bfs(start):
	queue = [start]
	visited[start] = 1

	while queue:
		v = queue.pop(0)
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = visited[v] + 1

	return visited.count(2) + visited.count(3)

print(bfs(1))