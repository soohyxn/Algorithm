import sys
input = sys.stdin.readline

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()

start, end = lines[0] # 처음 시작점, 끝점
ans = 0 # 선의 총길이

for i in range(1, N):
    x, y = lines[i] # 현재 선의 시작점, 끝점

    # 선이 겹치는 경우 끝점 업데이트
    if end > x:
        end = max(end, y)
    # 선이 겹치지 않는 경우 다음 선으로 업데이트
    else:
        ans += end - start
        start, end = x, y

ans += end - start # 가장 마지막 선길이를 더해준다
print(ans)