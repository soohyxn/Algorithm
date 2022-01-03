from collections import defaultdict

T = int(input())
for _ in range(T):
    n = int(input())
    cloth = defaultdict(list)
    answer = 1

    for _ in range(n):
        a, b = input().split()
        cloth[b].append(a)

    for k, v in cloth.items():
        answer *= len(v) + 1
    print(answer-1)