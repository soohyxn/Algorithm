# 10진수를 k진수로 변환
def convert_k(n, k):
    tmp = ''
    while n:
        tmp += str(n % k)
        n //= k
    return tmp[::-1]

# 소수 판별
def isPrime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = convert_k(n, k)
    primes = num.split('0') # 조건에 해당하는 숫자를 뽑는다
    
    for prime in primes:
        if prime != '' and prime != '1': # 2이상인 숫자인 경우
            if isPrime(int(prime)):
                answer += 1
            
    return answer