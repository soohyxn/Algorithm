from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
answer = 0 # 식의 최대값

for per in permutations(nums, n):
    result = 0 # 식의 값
    for i in range(len(per)-1):
        result += abs(per[i] - per[i+1])
    answer = max(answer, result)

print(answer)