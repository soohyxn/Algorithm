n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
r_max, r_min = -1e9, 1e9

def dfs(depth, result, plus, minus, multiply, divide):
	global r_max, r_min
	if depth == n:
		r_max = max(r_max, result)
		r_min = min(r_min, result)
		return

	if plus: 
		dfs(depth + 1, result + nums[depth], plus - 1, minus, multiply, divide)
	if minus:
		dfs(depth + 1, result - nums[depth], plus, minus - 1, multiply, divide)
	if multiply:
		dfs(depth + 1, result * nums[depth], plus, minus, multiply - 1, divide)
	if divide:
		dfs(depth + 1, int(result / nums[depth]), plus, minus, multiply, divide - 1)

dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(r_max)
print(r_min)