def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key = len)
    
    for i in s:
        nums = i.split(',')
        for num in nums:
            if int(num) not in answer:
                answer.append(int(num))
    
    return answer