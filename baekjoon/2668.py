from collections import defaultdict

n = int(input())
graph = defaultdict(list)
visited = [0] * (n+1)
ans = []

# 숫자 연결 관계 찾기
for i in range(1, n+1):
    j = int(input())
    graph[j].append(i)

def dfs(num):
    for next in graph[num]:
        if visited[next]: # 사이클이 있다면 같은 집합이므로 저장
            ans.append(next)
        else: # 아니라면 계속 탐색
            visited[next] = 1
            dfs(next)
            visited[next] = 0

# 모든 숫자 완전 탐색
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = 1
        dfs(i)
        visited[i] = 0

print(len(ans))
for i in ans: print(i)