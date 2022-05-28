n = int(input())
sol = list(map(int, input().split()))
sol.sort()

l, r = 0, n-1 # 투포인터
result = sol[l] + sol[r] # 용액의 합
al, ar = l, r

while l < r:
    mix = sol[l] + sol[r]

    if abs(mix) < abs(result): # 새로운 용액의 합이 더 작다면 갱신
        result = mix
        al, ar = l, r

    if mix == 0:
        break
    elif mix < 0:
        l += 1
    else:
        r -= 1

print(sol[al], sol[ar])