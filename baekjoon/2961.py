from itertools import combinations

N = int(input())
taste = [list(map(int, input().split())) for _ in range(N)]
coms = [combinations(taste, i) for i in range(1, N+1)]
answer = 1e9

for com in coms:
    for c in com:
        sour, bitter = 1, 0
        for s, b in c:
            sour *= s
            bitter += b
        answer = min(answer, abs(sour - bitter))
print(answer)