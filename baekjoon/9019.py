from collections import deque

t = int(input())

def bfs(start, target):
    queue = deque([[start, '']])

    while queue:
        num, command = queue.popleft()
        # a -> b로 변환이 된 경우 결과를 출력하고 리턴
        if num == target:
            print(command)
            return

        # 네가지 명령어로 숫자를 변환한다
        # D
        tmp = num * 2 % 10000
        if not checked[tmp]:
            queue.append([tmp, command + 'D'])
            checked[tmp] = 1

        # S
        if num == 0: tmp = 9999
        else: tmp = num - 1
        if not checked[tmp]:
            queue.append([tmp, command + 'S'])
            checked[tmp] = 1

        # L
        tmp = num % 1000 * 10 + num // 1000
        if not checked[tmp]:
            queue.append([tmp, command + 'L'])
            checked[tmp] = 1

        # R
        tmp = num % 10 * 1000 + num // 10
        if not checked[tmp]:
            queue.append([tmp, command + 'R'])
            checked[tmp] = 1

for _ in range(t):
    a, b = map(int, input().split())
    checked = [0] * 10000 # 사용된 숫자인지 확인 리스트
    checked[a] = 1
    bfs(a, b)