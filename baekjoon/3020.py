n, h = map(int, input().split())
down, up, total = [0] * (h+1), [0] * (h+1), [0] * (h+1) # 높이에 따른 종유석, 석순, 최종 개수

for i in range(n):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

# 누적합
for i in range(h-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

# 높이에 따른 파괴해야 하는 장애물 최종 개수 구하기
for i in range(1, h+1):
    total[i] = up[i] + down[h-i+1]

total = total[1:]
print(min(total), total.count(min(total)))