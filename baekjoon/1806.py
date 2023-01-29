N, S = map(int, input().split())
nums = list(map(int, input().split()))
sum = [0] * (N+1) # 누적합
left, right = 0, 1 # 투포인터
ans = 1e9 # 최소 길이

# 누적합 구하기
for i in range(1, N+1):
    sum[i] = sum[i-1] + nums[i-1]

# 투포인터
while left <= N and right <= N:
    result = sum[right] - sum[left] # 부분합

    if result >= S: # 부분합이 S이상이면 길이 갱신, 왼쪽 포인터 이동
        ans = min(ans, right - left)
        left += 1
    else: # 아니라면 오른쪽 포인터 이동
        right += 1

print(0 if ans == 1e9 else ans)