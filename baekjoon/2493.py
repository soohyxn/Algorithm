n = int(input())
towers = list(map(int, input().split()))
stack = []
answer = [0] * n

for i in range(n):
    while stack:
        if stack[-1][0] > towers[i]:
            answer[i] = stack[-1][1] + 1
            break
        else:
            stack.pop()
    stack.append((towers[i], i))

print(*answer)