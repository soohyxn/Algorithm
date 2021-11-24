nums = list(map(int, input().split()))
length = len(nums)

while nums != [1, 2, 3, 4, 5]:
	for i in range(length-1):
		if nums[i] > nums[i+1]:
			nums[i], nums[i+1] = nums[i+1], nums[i]
			print(*nums)