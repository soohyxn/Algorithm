import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = dict()
ans = N

for _ in range(N):
    word = input().rstrip()
    words[word] = 1

for _ in range(M):
    memos = list(input().rstrip().split(','))
    for memo in memos:
        if memo in words.keys() and words[memo] == 1:
            words[memo] -= 1
            ans -= 1
    print(ans)