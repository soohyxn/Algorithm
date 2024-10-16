from itertools import combinations

n, l, r, x = map(int, input().split())
levels = list(map(int, input().split()))
answer = 0

# 2개 이상의 문제를 뽑는 모든 경우를 탐색한다
for i in range(2, n+1):
    # 가능한 모든 문제의 조합
    cases = list(combinations(levels, i))
    
    for case in cases:
        # 난이도의 합과 난이도 차이 조건을 만족하는지 체크
        if l <= sum(case) <= r and max(case) - min(case) >= x:
            answer += 1
        
print(answer)