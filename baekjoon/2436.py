g, l = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

div = l // g
x, y = 1, div # 합이 최소가 되는 두 자연수
for i in range(1, div//2+1):
    if div % i == 0:
        a, b = i, div // i
        # 서로소가 아닌 경우
        if gcd(a, b) != 1:
            continue
        # 합이 최소인 경우
        if a + b < x + y:
            x, y = a, b

print(x * g, y * g)