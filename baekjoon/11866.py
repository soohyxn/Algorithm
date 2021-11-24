n, k = map(int, input().split())
people = [i for i in range(1, n+1)]

idx = 0
delete = []

while people:
	idx = (idx + k - 1) % len(people)
	delete.append(people.pop(idx))
print('<' + str(delete)[1: -1] + '>')