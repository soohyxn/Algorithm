from collections import deque

def solution(queue1, queue2):
    deque1, deque2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(deque1), sum(deque2)
    
    # 최소 작업 횟수 구하기
    for i in range(len(queue1) * 3):
        # 각 큐의 원소 합이 같지 않으면 원소 이동
        if sum1 > sum2:
            num = deque1.popleft()
            deque2.append(num)
            sum1 -= num
            sum2 += num
        elif sum1 < sum2:
            num = deque2.popleft()
            deque1.append(num)
            sum1 += num
            sum2 -= num
        # 각 큐의 원소 합이 같은 경우 리턴
        else:
            return i
        
    return -1