import sys, heapq
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort()

queue = []
heapq.heappush(queue, time[0][1])

for i in range(1, N):
    if time[i][0] < queue[0]: # 현재 수업이 끝나는 시간보다 다음 수업 시작 시간이 빠르면
        heapq.heappush(queue, time[i][1]) # 강의실 추가
    else: # 현재 강의실에서 이어서 수업을 할 수 있다면
        heapq.heappop(queue) # 현재 수업 제거
        heapq.heappush(queue, time[i][1]) # 다음 수업 추가

print(len(queue))