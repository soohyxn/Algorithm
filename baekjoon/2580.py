import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
flag = False

def get_possible(i, j):
	possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	for k in range(9):
		if sudoku[i][k] in possible:
			possible.remove(sudoku[i][k])
		if sudoku[k][j] in possible:
			possible.remove(sudoku[k][j])

	for a in range(i//3*3, i//3*3+3):
		for b in range(j//3*3, j//3*3+3):
			if sudoku[a][b] in possible:
				possible.remove(sudoku[a][b])

	return possible

def dfs(n):
	global flag
	
	if flag:
		return
		
	if n == len(zeros):
		for row in sudoku:
			print(*row)
		flag = True
		return
	else:
		i, j = zeros[n]
		possible = get_possible(i, j)

		for num in possible:
			sudoku[i][j] = num
			dfs(n + 1)
			sudoku[i][j] = 0

dfs(0)	