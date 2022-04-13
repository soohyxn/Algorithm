def solution(s):
    answer, num = '', ''
    words = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    for c in s:
        if num in words.keys(): # 숫자에 대응하는 영단어인 경우 숫자로 바꾸어 저장
            answer += words[num]
            num = ''
            
        if c.isdigit(): # 숫자인 경우
            answer += c
        else:
            num += c
            
    if num: # 남아있는 영단어 처리
        answer += words[num]
        
    return int(answer)