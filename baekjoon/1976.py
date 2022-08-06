N, M = int(input()), int(input())
parent = [i for i in range(N)]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

# 유니온 파인드
for i in range(N):
    graph = list(map(int, input().split()))
    for j in range(N):
        if graph[j] == 1:
            union(i, j)

path = list(map(int, input().split()))
start = parent[path[0]-1] # 출발 도시의 부모
for i in range(1, M):
    # 현재 도시와 출발 도시가 같은 집합이 아닌 경우
    if parent[path[i]-1] != start:
        print('NO')
        break
else:
    print('YES')