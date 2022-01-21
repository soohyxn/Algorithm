# 문자열을 u, v로 분리하기
def divide(p):
    open = 0
    close = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open += 1
        else:
            close += 1
            
        if open == close:
            return p[:i+1], p[i+1:]

# 올바른 문자열인지 확인하기
def isBalanced(p):
    stack = []
    
    for s in p:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
    
    return True

def solution(p):
    # 과정 1
    if not p:
        return ''
    
    # 과정 2
    u, v = divide(p)
    
    # 과정 3
    if isBalanced(u):
        # 과정 3-1
        return u + solution(v)
    # 과정 4
    else:
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'
        
        # 과정 4-4
        for i in range(1, len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
                
        # 과정 4-5
        return answer