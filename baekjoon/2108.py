import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
	nums.append(int(sys.stdin.readline()))

print(round(sum(nums) / n))

nums.sort()
print(nums[n//2])

count = Counter(nums).most_common()
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

print(max(nums) - min(nums))