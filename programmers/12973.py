def solution(s):
    stack = []

    for c in s:
        if stack:
            if c == stack[-1]:
                stack.pop()
                continue
        stack.append(c)
    
    if stack:
        return 0
    else:
        return 1