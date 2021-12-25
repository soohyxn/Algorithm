N, K = map(int, input().split())
nums = [x for x in range(1, N+1)]
start = K-1
print('<', end='')
for _ in range(N-1):
    print(nums[start], end=', ')
    nums.pop(start)
    start = (start + K - 1) % len(nums)
print(f'{nums[-1]}>')