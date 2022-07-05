T = int(input())

def recur(num, exp):
    # 수식이 완성된 경우
    if num == N+1:
        # 수식의 값이 0인 경우 출력
        if eval(exp.replace(' ', '')) == 0: print(exp)
        return

    recur(num+1, exp + ' ' + str(num))
    recur(num+1, exp + '+' + str(num))
    recur(num+1, exp + '-' + str(num))

    
for _ in range(T):
    N = int(input())
    recur(2, '1')
    print()