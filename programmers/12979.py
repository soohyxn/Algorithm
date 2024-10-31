import math

def solution(n, stations, w):
    answer = 0
    dist = [] # 전파가 안되는 구간 길이 리스트
    
    # 맨 앞
    dist.append(stations[0]-w-1)
    
    # 중간
    for i in range(1, len(stations)):
        dist.append((stations[i]-w-1) - (stations[i-1]+w))
    
    # 맨 뒤
    dist.append(n-(stations[-1]+w))
    
    # 증설해야 할 기지국 최소 개수 구하기
    for d in dist:
        if d > 0:
            answer += math.ceil(d / (2*w+1))

    return answer