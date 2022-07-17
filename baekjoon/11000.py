import sys, heapq
input = sys.stdin.readline

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort() # 시작시간 -> 끝시간 기준 정렬

heap = []
heapq.heappush(heap, classes[0][1])

for i in range(1, N):
    if classes[i][0] >= heap[0]: # 현재 수업을 수업이 끝나는 강의실에서 이어서 할 수 있는 경우
        heapq.heappop(heap)
    heapq.heappush(heap, classes[i][1]) # 현재 수업 추가

print(len(heap))