n = int(input())
persons = []

for _ in range(n):
	person = list(map(int, input().split()))
	persons.append(person)

for m in persons:
	rank = 1

	for y in persons:
		if m[0] != y[0] and m[1] != y[1]:
			if m[0] < y[0] and m[1] < y[1]:
				rank += 1

	print(rank, end = " ")