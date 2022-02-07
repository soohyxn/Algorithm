import heapq

n = int(input())
heap = []

for _ in range(n):
    if not heap:
        heap = list(map(int, input().split()))
        heapq.heapify(heap)
    else:
        tmp = list(map(int, input().split()))
        for i in range(n):
            if tmp[i] >= heap[0]: # 슬라이딩 윈도우
                heapq.heappop(heap)
                heapq.heappush(heap, tmp[i])

print(heap[0]) # n번째 큰 수