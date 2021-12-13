num = input()
min, max = '', ''
m = 0 # K가 나오기 전 M의 개수

for n in num:
    if n == 'M': # M일 경우 개수 증가
        m += 1
    else: # K일 경우 m의 값에 따른 최소, 최대를 구한다
        if m > 0:
            min += str(10 ** m + 5)
            max += str(5 * (10 ** m))
        else:
            min += '5'
            max += '5'
        m = 0

# 마지막이 M으로 끝났을 경우 처리
if m > 0:
    min += str(10 ** (m-1))
    max += '1' * m

print(max)
print(min)