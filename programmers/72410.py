def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = ''.join([c for c in new_id if c.isalnum() or c in '-_.'])
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # 4단계
    new_id = new_id.strip('.')
    # 5단계
    if len(new_id) == 0: new_id = 'a'
    # 6단계
    if len(new_id) >= 16: new_id = new_id[:15].strip('.')
    # 7단계
    if len(new_id) <= 2: new_id = new_id + new_id[-1] * (3 - len(new_id))
        
    return new_id