n = int(input())
postfix = input()
nums = [int(input()) for _ in range(n)]

stack = []
for p in postfix:
	if 'A' <= p <= 'Z':
		stack.append(nums[ord(p) - ord('A')])
	else:
		b = stack.pop()
		a = stack.pop()

		if p == '+': 
			stack.append(a + b)
		elif p == '-':
			stack.append(a - b)
		elif p == '*':
			stack.append(a * b)
		elif p == '/':
			stack.append(a / b)

print('%.2f' % stack[0])