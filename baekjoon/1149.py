n = int(input())
house = [[0, 0, 0] for _ in range(n+1)]
for i in range(1, n+1):
    house[i] = list(map(int, input().split()))

for i in range(1, n+1):
    house[i][0] += min(house[i-1][1], house[i-1][2])
    house[i][1] += min(house[i-1][0], house[i-1][2])
    house[i][2] += min(house[i-1][0], house[i-1][1])
print(min(house[n]))