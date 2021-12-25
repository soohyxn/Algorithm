while True:
    str = input()
    if str == '.':
        break

    stack = []
    for s in str:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                break

    if stack:
        print('no')
    else:
        print('yes')