from collections import defaultdict
import math

def solution(fees, records):
    dt, df, ut, uf = fees # 기본시간, 기본요금, 단위시간, 단위요금
    cars = defaultdict(list) # 차량별 입/출차 내역
    answer = []
    
    for record in records:
        time, num, history = record.split(' ')
        h, m = map(int, time.split(":"))
        cars[num].append([h * 60 + m, history])
    
    cars = list(cars.items())
    cars.sort(key = lambda x: x[0]) # 차량번호 작은 순으로 정렬
    
    # 차량별 주차요금 구하기
    for num, info in cars:
        total = 0 # 누적 주차 시간
        for time, history in info:
            if history == 'IN':
                total -= time
            else:
                total += time
        
        if info[-1][1] == 'IN': # 입차된 후 출차 내역이 없는 경우
             total += 23 * 60 + 59
            
        if total <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((total - dt) / ut) * uf)
    
    return answer