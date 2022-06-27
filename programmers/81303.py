def solution(n, k, cmd):
    table = {i: [i-1, i+1] for i in range(n)}
    table[0], table[n-1] = [None, 1], [n-2, None]
    now = k # 현재 행
    stack = []
    answer = ['O'] * n
    
    for c in cmd:
        # X칸 위의 행 선택하기
        if c[0] == 'U':
            for _ in range(int(c[2:])): now = table[now][0]
        # X칸 아래의 행 선택하기
        elif c[0] == 'D':
            for _ in range(int(c[2:])): now = table[now][1]
        # 현재 행 삭제하기
        elif c[0] == 'C':
            answer[now] = 'X'
            prev, next = table[now]
            stack.append([now, prev, next])
            
            # 현재 행 변경
            if next == None:
                now = table[now][0]
            else:
                now = table[now][1]
        
            # 표 연결 정보 변경
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev
        # 최근 삭제한 행 복구하기
        elif c[0] == 'Z':
            idx, prev, next = stack.pop()
            answer[idx] = 'O'
            
            # 표 연결 정보 변경
            if prev == None:
                table[next][0] = idx
            elif next == None:
                table[prev][1] = idx
            else:
                table[next][0] = idx
                table[prev][1] = idx
                
    return ''.join(answer)