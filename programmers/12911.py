def solution(n):
    cn = bin(n).count('1')
    
    for a in range(n+1, 10000001):
        an = bin(a).count('1')
        if an == cn:
            return a