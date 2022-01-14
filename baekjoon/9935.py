s = input()
exp = input()
l = len(exp)
answer = []

for c in s:
    answer.append(c)
    if c == exp[-1] and ''.join(answer[-l:]) == exp: # 폭발할 문자열과 같으면 삭제
        del answer[-l:]

if answer:
    print(''.join(answer))
else:
    print('FRULA')