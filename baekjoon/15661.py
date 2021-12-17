from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9

for i in range(1, n//2+1):
    com = list(combinations(range(n), i)) # 1부터 N//2까지 start 조합
    for start in com:
        link = [x for x in range(n) if x not in start] # link = start에 속해 있지 않은 사람
        s_start, s_link = 0, 0
    
        # 각 팀의 능력치 계산
        for x, y in combinations(start, 2):
            s_start += s[x][y] + s[y][x]
    
        for x, y in combinations(link, 2):
            s_link += s[x][y] + s[y][x]
    
        answer = min(answer, abs(s_start - s_link))
        if answer == 0:
            break

print(answer)