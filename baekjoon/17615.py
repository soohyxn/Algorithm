n = int(input())
s = input()

red = s.count('R')
blue = n - red
ans = min(red, blue)

# 오른쪽으로 옮기기
cnt = 0
for i in range(n):
    if s[0] != s[i]:
        break
    cnt += 1
if s[0] == 'R':
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)

# 왼쪽으로 옮기기
cnt = 0
for i in range(n-1, -1, -1):
    if s[-1] != s[i]:
        break
    cnt += 1
if s[-1] == 'R':
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)

print(ans)