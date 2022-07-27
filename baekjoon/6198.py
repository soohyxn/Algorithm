N = int(input())
h = [int(input()) for _ in range(N)]
stack = []
ans = 0 # 정원을 확인할 수 있는 총합

for i in range(N):
    # 현재 빌딩을 볼 수 없을 때까지 스택에서 빌딩 제거
    while stack and h[i] >= stack[-1]:
        stack.pop()

    stack.append(h[i]) # 스택에 현재 빌딩 추가
    ans += len(stack) - 1 # 총합에 현재 빌딩을 볼 수 있는 수 추가

print(ans)