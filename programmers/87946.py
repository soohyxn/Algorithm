from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for com in permutations(dungeons, len(dungeons)):
        cnt, z = 0, k
        for i, j in com:
            if z >= i:
                z -= j
                cnt += 1
            else:
                break 
        answer = max(answer, cnt)
        
    return answer