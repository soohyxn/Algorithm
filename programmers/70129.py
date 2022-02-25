def solution(s):
    cnt, zero = 0, 0 # 이진변환 횟수, 제거된 0의 개수
    
    while s != '1':
        zero += s.count('0') # 0의 개수 세기
        s = s.replace('0', '') # '0' 제거하기
        s = bin(len(s))[2:] # 이진변환 하기
        cnt += 1
        
    return [cnt, zero]