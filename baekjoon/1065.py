num = int(input())
answer = 0

for i in range(1, num+1):
	if i <= 99:
		answer += 1
	else:
		nums = list(map(int, str(i)))	
		if nums[1] - nums[0] == nums[2] - nums[1]:
			answer += 1

print(answer)