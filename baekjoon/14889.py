import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False] * n
answer = 1e9

def dfs(depth, now):
	global answer
	
	if depth == n // 2:
		start, link =  0, 0
		
		for i in range(n):
			for j in range(n):
				if visited[i] and visited[j]:
					start += graph[i][j]
				elif not visited[i] and not visited[j]:
					link += graph[i][j]

		answer = min(answer, abs(start - link))
					
	for i in range(now, n):
		if not visited[i]:
			visited[i] = True
			dfs(depth + 1, i)
			visited[i] = False

dfs(0, 0)
print(answer)