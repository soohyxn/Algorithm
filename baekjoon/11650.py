import sys

n = int(sys.stdin.readline())
dot = []

for _ in range(n):
	x, y = map(int, sys.stdin.readline().split())
	dot.append([x, y])

dot.sort()

for d in dot:
	print(d[0], d[1])