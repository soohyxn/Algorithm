import math
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
ans = n

for i in a:
    cnt = math.ceil((i - b) / c)
    if cnt > 0: ans += cnt

print(ans) 