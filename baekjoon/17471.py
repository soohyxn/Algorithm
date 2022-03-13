from itertools import combinations
from collections import deque

n = int(input())
people = [0] + list(map(int, input().split())) # 구역별 인구수
graph = [[] for _ in range(n+1)] # 구역별 연결관계
nodes = [i for i in range(1, n+1)] # 구역 리스트
answer = 1e9 # 두 선거구의 인구 차이의 최소값

# 구역별 연결관계 구하기
for i in range(1, n+1):
    info = list(map(int, input().split()))
    for j in info[1:]:
        graph[i].append(j)

def bfs(nodes):
    queue = deque([nodes[0]])
    visited = set([nodes[0]])
    result = 0 # 인구합

    while queue:
        node = queue.popleft()
        result += people[node]
        for i in graph[node]:
            if i not in visited and i in nodes: # 아직 방문하지 않았으며 해당 선거구에 속해 있는 경우
                queue.append(i)
                visited.add(i)

    return result, len(visited)

# 두 선거구로 나눌 수 있는 모든 조합 탐색
for k in range(1, n//2+1):
    for com in combinations(nodes, k):
        # 두 선거구의 인구합과 연결되어 있는지 확인
        result1, n1 = bfs(com)
        result2, n2 = bfs([i for i in nodes if i not in com])
        # 두 선거구가 연결되어 있다면 인구 차이를 갱신
        if n1 + n2 == n:
            answer = min(answer, abs(result1 - result2))

print(answer) if answer != 1e9 else print(-1)