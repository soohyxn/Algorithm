from collections import defaultdict

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
cnt_nums = list(map(int, input().split()))
answer = defaultdict(int)

for n in nums:
    answer[n] += 1

for c in cnt_nums:
    print(answer[c], end=' ')