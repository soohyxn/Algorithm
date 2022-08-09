import re
N = int(input())

for _ in range(N):
    s = input()
    pattern = re.compile('(100+1+|01)+') # 정규 표현식
    print('YES' if pattern.fullmatch(s) else 'NO')