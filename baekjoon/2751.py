import sys

n = int(sys.stdin.readline())
nums = [] # 입력받은 숫자 리스트

for _ in range(n):
	nums.append(int(sys.stdin.readline()))

nums.sort() # 오름차순 정렬

for i in range(n):
    print(nums[i])