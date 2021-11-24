from collections import deque

t = int(input())
for _ in range(t):
    p_list = list(input())
    n = int(input())
    nums = deque(input()[1:-1].split(','))

    res, flag = 0, 0

    if n == 0:
        nums = []

    for p in p_list:
        if p == 'R':
            res += 1
        elif  p == 'D':
            if nums:
                if res % 2 == 0:
                    nums.popleft()
                else:
                    nums.pop()
            else:
                print('error')
                flag = 1
                break

    if flag == 0:
        if res % 2 != 0:
            nums.reverse()
        print('['+ ','.join(nums) +']')