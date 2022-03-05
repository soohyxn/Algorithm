S = list(input())
T = list(input())

while len(S) != len(T):
    last = T[-1]
    T.pop() # 마지막 문자 삭제
    if last == 'B': # 마지막 문자가 B라면 뒤집기
        T = T[::-1]

print(1) if S == T else print(0)