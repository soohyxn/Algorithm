from itertools import permutations

def sosu(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    
    for i in range(1, len(numbers)+1):
        pm = list(map(''.join, permutations(numbers, i)))
        for p in list(set(pm)):
            if sosu(int(p)):
                answer.append(int(p))
                
    return len(set(answer))