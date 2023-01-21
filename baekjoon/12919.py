import sys

S = input()
T = input()

def make(t):
    if len(t) == len(S):
        # S를 T로 바꿀 수 있다면 재귀 종료
        if t == S: 
            print(1)
            sys.exit()
        return

    # 마지막 문자가 A라면 제거한다
    if t[-1] == 'A':
        make(t[:-1])
    # 첫번째 문자가 B라면 제거하고 뒤집는다
    if t[0] == 'B':
        make(t[1::][::-1])

make(T)
print(0)