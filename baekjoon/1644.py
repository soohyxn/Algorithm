n = int(input())
num = [0, 0] + [1] * (n-1) # 소수 판별 리스트
ans = 0 # 연속된 소수의 합으로 나타낼 수 있는 경우의 수

# 에라토스테네스의 체로 소수 구하기
for i in range(2, int(n ** 0.5)+1):
    for j in range(i*2, n+1, i):
        if num[j]:
            num[j] = 0

prime = [i for i in range(2, n+1) if num[i]] # 소수 리스트
left, right = 0, 0

# 투 포인터로 경우의 수 구하기
while left <= n and right <= n:
    result = sum(prime[left: right+1])

    if result == n:
        ans += 1

    if result >= n:
        left += 1
    else:
        right += 1

print(ans)