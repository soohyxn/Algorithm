import heapq

def solution(n, works):
    # 작업량보다 야근량이 더 큰 경우
    if sum(works) < n: 
        return 0
    
    heap_works = [-w for w in works]
    heapq.heapify(heap_works)
    
    # 우선순위가 높은 것부터 야근 처리
    for _ in range(n):
        work = heapq.heappop(heap_works)
        work += 1
        heapq.heappush(heap_works, work)
    
    return sum([w ** 2 for w in heap_works])