import copy

# 키 90도 회전
def rotate(key):
    l = len(key)
    res = [[0] * l for _ in range(l)]
    
    for i in range(l):
        for j in range(l):
            res[j][l-1-i] = key[i][j]
    return res

# 자물쇠를 열 수 있는지 확인
def check(x, y, start, end, key, arr):
    # 자물쇠에 키 값 더하기
    for i in range(len(key)):
        for j in range(len(key)):
            arr[x+i][y+j] += key[i][j]
    
    for i in range(start, end):
        for j in range(start, end):
            if arr[i][j] != 1: # 자물쇠를 열 수 없는 경우
                return False
            
    return True

def solution(key, lock):
    start = len(key) - 1 # 자물쇠의 시작점
    end = start + len(lock) # 자물쇠의 끝점
    all = start * 2 + end # 확장한 자물쇠 크기
    new_lock = [[0] * all for _ in range(all)] # 확장한 자물쇠 리스트
    
    # 자물쇠 정보 저장
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[start+i][start+j] = lock[i][j]
            
    # 키를 회전시키면서 자물쇠를 열 수 있는지 확인
    for _ in range(4):
        key = rotate(key)
        for i in range(end):
            for j in range(end):
                if check(i, j, start, end, key, copy.deepcopy(new_lock)): 
                    return True
    return False