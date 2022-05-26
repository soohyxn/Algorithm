N, D = map(int, input().split())
shortcut = [list(map(int, input().split())) for _ in range(N)]
dist = [i for i in range(D+1)] # 각 위치의 운전 최소 거리

for i in range(D+1):
    # 이전 위치와 비교하여 거리 갱신
    dist[i] = min(dist[i], dist[i-1] + 1)

    # 지름길로 갈 수 있다면 거리 갱신
    for start, end, cost in shortcut:
        if i == start and end <= D:
            dist[end] = min(dist[end], dist[start] + cost)

print(dist[D])