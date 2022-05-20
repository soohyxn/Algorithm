def solution(n, t, m, timetable):
    answer = 0
    
    crew_time = [int(time[:2]) * 60 + int(time[3:]) for time in timetable] # 크루 도착시간 분단위로 변경
    crew_time.sort() # 시간순 정렬
    
    bus_time = [9 * 60 + t * i for i in range(n)] # 버스 시간
    
    i = 0 # 버스에 탈 크루의 인덱스
    for time in bus_time:
        cnt = 0 # 버스에 타는 크루 수
        while cnt < m and i < len(crew_time) and crew_time[i] <= time:
            cnt += 1
            i += 1
        if cnt < m: # 버스에 자리에 남았으면 탑승
            answer = time
        else: # 버스에 자리가 없으면 마지막 크루보다 1분 전 도착
            answer = crew_time[i-1] - 1
            
    return str(answer//60).zfill(2) + ':' + str(answer%60).zfill(2)