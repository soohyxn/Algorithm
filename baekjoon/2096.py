n = int(input())
max_dp = [0] * 3
min_dp = [0] * 3
max_tmp = [0] * 3
min_tmp = [0] * 3

for _ in range(n):
    nums = list(map(int, input().split()))
    
    for j in range(3):
        if j == 0:
            max_tmp[j] = nums[j] + max(max_dp[j], max_dp[j+1])
            min_tmp[j] = nums[j] + min(min_dp[j], min_dp[j+1])
        elif j == 1:
            max_tmp[j] = nums[j] + max(max_dp[j-1], max_dp[j], max_dp[j+1])
            min_tmp[j] = nums[j] + min(min_dp[j-1], min_dp[j], min_dp[j+1])
        else:
            max_tmp[j] = nums[j] + max(max_dp[j-1], max_dp[j])
            min_tmp[j] = nums[j] + min(min_dp[j-1], min_dp[j])
    
    for i in range(3):
        max_dp[i] = max_tmp[i]
        min_dp[i] = min_tmp[i]

print(max(max_dp), min(min_dp))