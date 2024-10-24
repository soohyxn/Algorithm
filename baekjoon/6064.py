t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    k = x # k번째 해

    while k <= m * n:
        # k번째 해를 구하면 리턴
        if (k - x) % m == 0 and (k - y) % n == 0:
            print(k)
            break
        k += m
    else:
        # 유효하지 않은 해이면 -1 리턴
        print(-1)