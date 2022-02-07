n = int(input())
sol = list(map(int, input().split()))
sol.sort()

l, r = 0, n-1
result = sol[l] + sol[r]
al, ar = l, r

while l < r:
    mix = sol[l] + sol[r]

    if abs(mix) < abs(result):
        result = mix
        al, ar = l, r

    if mix == 0:
        break
    elif mix < 0:
        l += 1
    else:
        r -= 1

print(sol[al], sol[ar])