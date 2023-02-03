N = int(input())
towers = list(map(int, input().split()))
stack = []
ans = [0] * N

for i in range(N):
    # 수신탑을 구한다
    while stack:
        if stack[-1][0] > towers[i]: # 레이저를 수신할 수 있다면 저장 후 종료
            ans[i] = stack[-1][1]
            break
        else: # 그렇지 않다면 스택에서 제거
            stack.pop()
    stack.append([towers[i], i+1])

print(*ans)