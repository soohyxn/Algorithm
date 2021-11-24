import sys

n = int(sys.stdin.readline()) # 점의 개수
nums = []
# 숫자 입력 받기
for _ in range(n):
	x, y = map(int, sys.stdin.readline().split())
	nums.append([x, y])

nums.sort(key = lambda x: (x[1], x[0]))

for num in nums:
	print(num[0], num[1])