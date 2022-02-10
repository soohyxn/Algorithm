def solution(files):
    answer = []
    
    for file in files:
        head, number, tail = '', '', ''
        
        for i in range(len(file)):
            if file[i].isdigit(): # 숫자가 나오면 head, number 분리
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):
                    if not number[j].isdigit(): # number에서 숫자가 아닌 문자가 나오면 tail, number 분리
                        tail = number[j:]
                        number = number[:j]
                        break

                answer.append([head, number, tail]) # 분리한 것을 저장
                break
    
    answer.sort(key = lambda x: (x[0].lower(), int(x[1]))) # head 사전순, number 오름차순 정렬
            
    return [''.join(a) for a in answer]