S = input()
flag = False # 태그 확인 여부
word = ''
answer = ''

for s in S:
    if flag == False:
        if s == '<':
            flag = True
            word += s
        elif s == ' ': # 중간 저장
            word += s
            answer += word
            word = ''
        else: # 뒤집어서 저장
            word = s + word
    else:
        word += s
        if s == '>':
            flag = False
            answer += word
            word = ''
print(answer + word)