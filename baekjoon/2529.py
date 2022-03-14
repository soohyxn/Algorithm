from itertools import permutations

k = int(input())
sign = list(input().split())
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = []

for per in permutations(num, k+1):
    for i in range(k):
        if sign[i] == '<' and per[i] > per[i+1]:
            break
        elif sign[i] == '>' and per[i] < per[i+1]:
            break
    else:
        answer.append(''.join(map(str, per)))

print(max(answer))
print(min(answer))