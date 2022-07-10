from itertools import combinations

L, C = map(int, input().split())
alpha = list(input().split())
alpha.sort()

# 가능한 암호 구하기
for com in combinations(alpha, L):
    cnt = 0 # 모음의 개수
    for c in com:
        if c in 'aeiou':
            cnt += 1
    
    if cnt >= 1 and L - cnt >= 2: # 모음이 최소 1개 이상, 자음이 최소 2개 이상인 경우
        print(''.join(com))