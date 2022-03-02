from collections import deque

# 올바른 괄호인지 확인
def check(s):
    stack = []
    
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if not stack:
                return False
            
            p = stack.pop()
            
            # 올바른 괄호가 아니라면 return False
            if c == ')' and p != '(':
                return False
            if c == ']' and p != '[':
                return False
            if c == '}' and p != '{':
                return False
            
    return len(stack) == 0

def solution(s):
    answer = 0 # 올바른 괄호 개수
    arr = deque(s)
    
    for _ in range(len(arr)):
        arr.rotate(-1) # 왼쪽으로 1칸 이동
        if check(arr):
            answer += 1
    
    return answer