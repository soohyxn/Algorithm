t = int(input())

for _ in range(t):
    n = int(input())
    pn = [input() for _ in range(n)]

    pn.sort()

    # 같은 숫자가 있는지 확인
    for i in range(n-1):
        if pn[i] == pn[i+1][0: len(pn[i])]:
            print('NO')
            break
    else:
        print('YES')