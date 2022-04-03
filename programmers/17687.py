# n진수로 변환하기
def convert(num, n):
    str = '0123456789ABCDEF'
    q, r = divmod(num, n) # 몫, 나머지
    
    return convert(q, n) + str[r] if q else str[r]

def solution(n, t, m, p):
    answer, result = '', ''
    
    # 숫자 -> n진수로 변환
    for i in range(m*t):
        result += convert(i, n)
        
    # 말해야하는 숫자 구하기
    while len(answer) < t:
        answer += result[p-1]
        p += m
    
    return answer