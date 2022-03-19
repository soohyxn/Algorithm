n = int(input())
neg, pos = [], [] # 음수, 양수 리스트
ans = 0 # 최대 합

for _ in range(n):
    num = int(input())
    if num == 1:
        ans += 1
    elif num > 1:
        pos.append(num)
    else:
        neg.append(num)

pos.sort(reverse=True)
neg.sort()

if len(pos) % 2 == 0:
    for i in range(0, len(pos), 2):
        ans += pos[i] * pos[i+1]
else:
    for i in range(0, len(pos)-1, 2):
        ans += pos[i] * pos[i+1]
    ans += pos[-1]

if len(neg) % 2 == 0:
    for i in range(0, len(neg), 2):
        ans += neg[i] * neg[i+1]
else:
    for i in range(0, len(neg)-1, 2):
        ans += neg[i] * neg[i+1]
    ans += neg[-1]

print(ans)