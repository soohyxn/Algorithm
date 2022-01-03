n = int(input())
ring = list(map(int, input().split()))

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

for i in range(1, n):
    g = gcd(ring[0], ring[i])
    print(f'{ring[0]//g}/{ring[i]//g}')