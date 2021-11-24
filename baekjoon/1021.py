from collections import deque

n, m = map(int, input().split())
value = list(map(int, input().split()))
deque = deque([i+1 for i in range(n)])
count = 0

for v in value:
	if v == deque[0]:
		deque.popleft()
		continue

	idx = deque.index(v)
	if idx > len(deque) // 2:
		deque.rotate(len(deque) - idx)
		count += (len(deque) - idx)
	else:
		deque.rotate(-idx)
		count += idx
	deque.popleft()

print(count)