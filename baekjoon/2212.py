N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().split())))

dist = [sensors[i+1] - sensors[i] for i in range(N-1)] # 센서들 거리 차이
dist.sort()

print(sum(dist[:N-K])) # 수신 가능한 영역의 최소 거리 합