n = list(map(int, input()))
n.sort(reverse=True)

if 0 not in n:
    print(-1)
else:
    s = sum(n)
    if s % 3 == 0:
        print(''.join(map(str, n)))
    else:
        print(-1)