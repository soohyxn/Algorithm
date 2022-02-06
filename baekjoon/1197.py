V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
parent = [x for x in range(V+1)]
edges = []
ans = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])
edges.sort() # 가중치가 작은 순으로 정렬

# 특정 원소가 속한 집합 찾기
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA > rootB:
        parent[rootA] = rootB
    else:
        parent[rootB] = rootA

for cost, a, b in edges:
    if find(a) != find(b): # 사이클이 발생하지 않는 경우에 연결한다
        union(a, b)
        ans += cost

print(ans)