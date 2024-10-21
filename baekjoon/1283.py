n = int(input())
words = [list(input().split()) for _ in range(n)]
shortcut_key = [] # 단축키 리스트

for word in words:
    for i in range(len(word)):
        # 1. 첫글자가 단축키로 지정되어 있는지 체크하여 단어에 단축키 표시하여 출력한다
        if word[i][0].upper() not in shortcut_key:
            shortcut_key.append(word[i][0].upper())
            word[i] = "[" + word[i][0] + "]" + word[i][1:]
            print(' '.join(word))
            break
    else:
        # 2. 왼쪽 알파벳부터 단축키로 지정되어 있는지 체크하여 단어에 단축키 표시하여 출력한다 (모든 첫글자가 단축키로 지정되어 있는 경우)
        for i in range(len(word)):
            flag = False # 단축키 지정 여부

            for j in range(len(word[i])):
                if word[i][j].upper() not in shortcut_key:
                    shortcut_key.append(word[i][j].upper())
                    word[i] = word[i][:j] + "[" + word[i][j] + "]" + word[i][j+1:]
                    flag = True
                    print(' '.join(word))
                    break
            
            if flag:
                break
        # 3. 어떠한 것도 단축키로 지정할 수 없는 경우 단어 그대로 출력한다
        else:
            print(*word)