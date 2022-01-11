S = input()
num = ''
zero, one = 0, 0

for s in S:
    if s != num:
        if s == '0':
            zero += 1
        else:
            one += 1
        num = s
print(min(zero, one))