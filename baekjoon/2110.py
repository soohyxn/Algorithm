N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()
low, high = 1, house[-1] - house[0]

# 이분탐색
while low <= high:
    mid = (low + high) // 2
    cur = house[0] # 공유기를 설치한 마지막 위치
    cnt = 1 # 설치한 공유기 개수

    # 공유기 설치
    for i in range(1, N):
        if house[i] >= cur + mid:
            cur = house[i]
            cnt += 1

    if cnt >= C:
        low = mid + 1
    else:
        high = mid - 1

print(high)