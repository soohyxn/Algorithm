N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.sort(reverse=True)
count = 0

for c in coin:
    if  c <= K:
        count += K // c
        K %= c
print(count)