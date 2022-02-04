import math

def solution(n, words):
    answer = [0, 0]
    talk = [words[0]]

    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in talk: # 끝말잇기가 아니거나 이미 나온 단어를 말한 경우
            answer = [(i % n) + 1, math.ceil((i+1) / n)]
            break
        talk.append(words[i])

    return answer