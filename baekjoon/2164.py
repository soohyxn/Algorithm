from collections import deque

n = int(input())
nums = deque([i for i in range(1, n+1)])

while nums:
	if len(nums) == 1:
		break
		
	nums.popleft()
	top = nums.popleft()
	nums.append(top)

print(*list(nums))