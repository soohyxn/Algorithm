n, m = map(int, input().split()) 
chess = [] 
paint = [] 

for _ in range(n):
	chess.append(input())
	
for a in range(n-7):
	for b in range(m-7):
		start_w = 0 
		start_b = 0 

		for i in range(a, a+8):
			for j in range(b, b+8):
				if i % 2 == 0 and j % 2 == 0:
					if chess[i][j] != 'W': start_w += 1
					if chess[i][j] != 'B': start_b += 1
				elif i % 2 == 1 and j % 2 == 1:
					if chess[i][j] != 'W': start_w += 1
					if chess[i][j] != 'B': start_b += 1
				else: 
					if chess[i][j] != 'B': start_w += 1
					if chess[i][j] != 'W': start_b += 1

		paint.append(start_w)	
		paint.append(start_b)

print(min(paint)) 