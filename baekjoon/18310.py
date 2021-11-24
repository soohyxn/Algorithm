n = int(input())
house = list(map(int, input().split()))

house.sort()

print(house[int((n-1)/2)])