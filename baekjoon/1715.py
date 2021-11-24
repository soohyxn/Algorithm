import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))
answer = 0

while len(cards) != 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)

    result = first + second
    answer += result
    heapq.heappush(cards, result)

print(answer)