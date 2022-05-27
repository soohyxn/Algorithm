N, K = map(int, input().split())
nums = list(map(int, input().split()))
counter = [0] * (max(nums) + 1) # 연속부분수열에서 각 숫자의 개수
left, right = 0, 0 # 투 포인터
ans = 0

while right < N:
    if counter[nums[right]] < K:
        counter[nums[right]] += 1
        right += 1
    else:
        counter[nums[left]] -=1
        left += 1
    ans = max(ans, right - left)

print(ans)