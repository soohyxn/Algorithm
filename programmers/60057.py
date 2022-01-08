def solution(s):
    answer = 1e9
    
    for i in range(1, len(s)+1): # i = 자르는 단위
        com = '' # 압축된 문자열
        word = s[0:i] # 반복 문자열
        cnt = 1 # 반복 횟수
        for j in range(i, len(s), i):
            if word == s[j:j+i]: # 반복되는 문자열이면 횟수에 +1
                cnt += 1
            else: # 반복되지 않는다면
                # 반복횟수에 따른 처리
                if cnt == 1:
                    com += word
                else:
                    com += str(cnt) + word  
                # 반복 문자열, 횟수 초기화
                word = s[j:j+i]
                cnt = 1
        
        # 마지막에 남은 문자열 처리
        if cnt == 1:
            com += word
        else:
            com += str(cnt) + word
        answer = min(answer, len(com)) # 가장 짧은 길이 구하기
        
    return answer