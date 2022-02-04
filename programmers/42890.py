from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    coms = [] # 후보키 조합
    for i in range(1, col+1):
        coms.extend(combinations(range(col), i))
    
    candidate = [] # 가능한 후보키
    for com in coms:
        tmp = [tuple([r[c] for c in com]) for r in relation]
        
        if len(set(tmp)) == row: # 유일성 체크
            flag = True
            
            for cd in candidate:
                if set(cd).issubset(set(com)): # 최소성 체크
                    flag = False
                    break
            
            if flag: candidate.append(com)
    
    return len(candidate)