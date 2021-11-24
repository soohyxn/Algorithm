n, m = map(int, input().split())

not_listen = [input() for _ in range(n)]
not_look = [input() for _ in range(m)]

result = list(set(not_listen) & set(not_look))
result.sort()

print(len(result))
for r in result:
	print(r)