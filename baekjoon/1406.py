import sys
editor = list(sys.stdin.readline().strip())
stack = []
n = int(sys.stdin.readline())

for _ in range(n):
	cmd = sys.stdin.readline().split()

	if cmd[0] == 'L' and editor:
		stack.append(editor.pop())
	elif cmd[0] == 'D' and stack:
		editor.append(stack.pop())
	elif cmd[0] == 'B' and editor:
		editor.pop()
	elif cmd[0] == 'P':
		editor.append(cmd[1])

print("".join(editor + list(reversed(stack))))