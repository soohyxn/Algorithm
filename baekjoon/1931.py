n = int(input())
conf = [list(map(int, input().split())) for _ in range(n)]
conf.sort(key=lambda x: (x[1], x[0]))

count, end_time = 0, 0
for start, end in conf:
    if start >= end_time:
        end_time = end
        count += 1
print(count)