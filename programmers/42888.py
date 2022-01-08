from collections import defaultdict

def solution(records):
    person = defaultdict()
    answer = []
    
    # 최종 닉네임 구하기
    for record in records:
        record = record.split()
        if record[0] != 'Leave':
            person[record[1]] = record[2]
            
    # 최종 메시지 구하기
    for record in records:
        record = record.split()
        if record[0] == 'Enter':
            answer.append(f'{person[record[1]]}님이 들어왔습니다.')
        elif record[0] == 'Leave':
            answer.append(f'{person[record[1]]}님이 나갔습니다.')
    
    return answer