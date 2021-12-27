K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
low, high = 1, max(lan)

while low <= high:
    mid = (low + high) // 2
    count = [l // mid for l in lan]

    if sum(count) >= N:
        low = mid + 1
    else:
        high = mid - 1

print(high)