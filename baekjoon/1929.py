import math

start, end = map(int, input().split())
sosu = [True] * (end+1)

for i in range(2, int(math.sqrt(end+1))+1):
	if sosu[i]:                    
		for j in range(2*i, end+1, i):
			sosu[j] = False

for i in range(start, end+1):
	if i > 1 and sosu[i] == True:
		print(i)