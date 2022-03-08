answer = [0, 0] # 최종적으로 남는 0과 1의 개수

def comp(x, y, n, arr):
    global answer
    
    value = arr[x][y] # 시작값
    flag = True # 압축이 가능한지 확인
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != value: # 모든 수가 같은 값이 아니라면 압축이 불가능하다
                flag = False
                break
        if not flag: break
    
    if flag: # 압축이 가능한 경우 시작값에 따른 개수를 센다
        if value == 0: 
            answer[0] += 1
        else: 
            answer[1] += 1 
    else: # 압축이 불가능한 경우 영역을 쪼갠다
        comp(x, y, n//2, arr)
        comp(x+n//2, y, n//2, arr)
        comp(x, y+n//2, n//2, arr)
        comp(x+n//2, y+n//2, n//2, arr)

def solution(arr):
    comp(0, 0, len(arr), arr)
    
    return answer