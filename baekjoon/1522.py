s = input()
cnt_a = s.count('a')
ans = 1e9 # 최소 교환 횟수

for i in range(len(s)):
    cnt_b = 0
    for j in range(i, i+cnt_a): # 슬라이딩 윈도우
        if s[j % len(s)] == 'b':
            cnt_b += 1
    ans = min(ans, cnt_b)

print(ans)