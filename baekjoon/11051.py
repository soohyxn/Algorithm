N, K = map(int, input().split())
M = N - K
answer = 1

while N > K:
    answer *= N
    N -= 1
while M > 1:
    answer //= M
    M -= 1
print(answer % 10007)