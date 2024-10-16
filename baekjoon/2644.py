n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    # 촌수를 계산해야 할 사람을 찾으면 리턴
    if v == b:
        return
    
    # 부모-자식 관계인 다음 사람으로 넘어가서 탐색
    for next in graph[v]:
        # 아직 탐색하지 않은 경우, 촌수 계산
        if visited[next] == -1:
            visited[next] = visited[v] + 1
            dfs(next)

visited[a] = 0
dfs(a)
print(visited[b])