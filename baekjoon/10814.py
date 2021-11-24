n = int(input())
people = []
for i in range(n):
	age, name = input().split()
	people.append((i, int(age), name))

people.sort(key = lambda x: (x[1], x[0]))

for p in people:
	print(p[1], p[2])