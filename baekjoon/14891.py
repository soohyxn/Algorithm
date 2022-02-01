from collections import deque

gear = [deque(map(int, input())) for _ in range(4)]
K = int(input())
rotate = deque(list(map(int, input().split())) for _ in range(K))

while rotate:
    num, dir = rotate.popleft() # 톱니바퀴 번호, 회전 방향
    num -= 1
    left, right = gear[num][6], gear[num][2] # 맞닿은 톱니바퀴
    gear[num].rotate(dir) # 현재 톱니바퀴 회전
    
    # 왼쪽 톱니바퀴 회전
    tmp = dir # 회전할 방향
    for i in range(num-1, -1, -1):
        if gear[i][2] != left:
            left = gear[i][6]
            tmp *= -1
            gear[i].rotate(tmp)
        else:
            break

    # 오른쪽 톱니바퀴 회전
    tmp = dir
    for i in range(num+1, 4):
        if gear[i][6] != right:
            right = gear[i][2]
            tmp *= -1
            gear[i].rotate(tmp)
        else:
            break

ans = sum([2 ** i for i in range(4) if gear[i][0] == 1]) # 톱니바퀴 점수 합
print(ans)