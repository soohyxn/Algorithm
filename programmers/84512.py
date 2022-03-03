words = [] # 길이 5이하의 모든 단어

def all_words(n, word):
    # 길이가 5가 되면 멈춘다
    if n == 5:
        return
    
    for c in ['A', 'E', 'I', 'O', 'U']:
        words.append(word + c) # 단어 만들기
        all_words(n+1, word + c)

def solution(word):
    all_words(0, '')
    
    return words.index(word) + 1