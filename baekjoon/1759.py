from itertools import combinations

L, C = map(int, input().split())
alpha = list(input().split())
alpha.sort()
combs = combinations(alpha, L)

for comb in combs:
    cnt = 0 # 모음 개수
    for c in comb:
        if c in 'aeiou':
            cnt += 1
    if cnt >= 1 and L-cnt >= 2: # 모음 최소 1개 이상, 자음 최소 2개 이상
        print(''.join(comb))