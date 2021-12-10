N = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))
price, m = 0, city[0]

for i in range(N-1):
    if city[i] < m:
        m = city[i]
    price += m * road[i]
print(price)