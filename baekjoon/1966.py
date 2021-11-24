t = int(input())

for _ in range(t):
	n, m = map(int, input().split())
	pr = list(map(int, input().split()))
	idx = list(range(len(pr)))
	order = 0

	while pr:
		if pr[0] >= max(pr):
			order += 1

			if idx[0] == m:
				print(order)
				break
			else:
				pr.pop(0)
				idx.pop(0)
		else:
			pr.append(pr.pop(0))
			idx.append(idx.pop(0))