h, w = map(int, input().split())
heights = list(map(int, input().split()))
ans = 0

for i in range(1, w-1):
    left = max(heights[:i])
    right = max(heights[i+1:])
    height = min(left, right)

    if heights[i] < height:
        ans += height - heights[i] # 고이는 빗물 높이

print(ans)