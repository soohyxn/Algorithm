N = int(input())
color = list(input())
count = {'R': 0, 'B': 0}
count[color[0]] = 1

for i in range(N):
    if color[i] != color[i-1]:
        count[color[i]] += 1
print(min(count['R'], count['B']) + 1)