from collections import deque

T = int(input())
for _ in range(T):
    p = list(input())
    n = int(input())
    x = deque(input()[1: -1].split(','))
    cnt, flag = 0, False # 배열을 뒤집는 횟수, 에러 발생 여부

    # 배열이 빈 경우
    if n == 0: x = deque([])

    # 함수 실행
    for i in p:
        # 배열을 뒤집는 경우
        if i == 'R':
            cnt += 1
        # 배열의 첫번째 수를 제거하는 경우
        else:
            # 배열이 비어있지 않다면 횟수에 따른 숫자 제거
            if x:
                if cnt % 2 == 0:
                    x.popleft()
                else:
                    x.pop()
            # 배열이 비어 있는 경우 에러 발생
            else:
                print('error')
                flag = True
                break
    
    # 에러가 발생하지 않았다면 결과 출력
    if not flag:
        if cnt % 2 == 1:
            x.reverse()
        print('[' + ','.join(x) + ']')