from itertools import combinations

def solution(nums):
    answer = 0

    for com in combinations(nums, 3):
        if prime(sum(com)):
            answer += 1

    return answer

# 소수인지 확인
def prime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True