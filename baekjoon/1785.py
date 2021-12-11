n = int(input())
p = [int(input()) for _ in range(n)]
p.sort(reverse=True)
answer = 0

for i in range(n):
    p[i] = p[i] - i
    if p[i] > 0:
        answer += p[i]
print(answer)