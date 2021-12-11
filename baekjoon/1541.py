exp = list(input().split('-'))
L = len(exp)

for i in range(L):
    s = list(map(int, exp[i].split('+')))
    exp[i] = sum(s)

answer = exp[0]
for i in range(1, L):
    answer -= exp[i]
print(answer)