def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery, pickup = 0, 0 # 배달, 수거 갯수
    
    # 최소 거리 구하기 = 먼 집부터 배달 및 수거한다
    for i in range(n-1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        # 트럭에 실을 수 있는 최대 갯수까지 배달 및 수거한다
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += (i + 1) * 2
        
    return answer