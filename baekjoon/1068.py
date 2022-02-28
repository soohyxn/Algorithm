n = int(input())
parent = list(map(int, input().split()))
graph = [[] for _ in range(n)] # 트리 그래프
delete = int(input())
root, ans = 0, 0 # 루트 노드, 리프 노드의 개수

# 트리 관계 구하기
for c, p in enumerate(parent):
    if p == -1: # 루트노드라면 루트노드 값 설정
        root = c
    else:# 루트노드가 아니라면 부모-자식 관계 연결
        graph[p].append(c)

def dfs(node):
    global ans

    # 리프 노드인 경우 개수에 +1 (자식 노드가 없거나 자식 노드에 삭제할 노드만 있는 경우)
    if len(graph[node]) <= 1:
        ans += 1 
        return

    # 자식 노드 탐색
    for i in graph[node]:
        if i != delete: # 삭제할 노드가 아니라면 탐색
            dfs(i)

if root == delete:
    print(0)
else:
    dfs(root)
    print(ans)