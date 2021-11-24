N, M = map(int, input().split())
tree = list(map(int, input().split()))
low, high = 1, max(tree)

while low <= high:
    mid = (low + high) // 2
    s = sum([t - mid for t in tree if t > mid])

    if s >= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)