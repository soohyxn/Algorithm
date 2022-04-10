def solution(lines):
    answer = 0
    start, end = [], [] # 시작시간, 끝시간 리스트
    
    for line in lines:
        time = line.split(" ")
        start_time, end_time = get_time(time[1], time[2]) # 해당 로그의 시작시간, 끝시간
        start.append(start_time)
        end.append(end_time)
    
    for i in range(len(lines)):
        cnt = 0 # 해당 끝시간 기준 1초간 처리하는 요청의 개수
        cur_end_time = end[i]
        for j in range(i, len(lines)):
            if cur_end_time > start[j] - 1000: # 1초간 처리할 수 있는 요청인 경우
                cnt += 1
        answer = max(answer, cnt)
        
    return answer

def get_time(s, t):
    hour = int(s[:2]) * 3600
    minute = int(s[3:5]) * 60
    second = int(s[6:8])
    milisecond = int(s[9:])
    t = t[:-1]
    
    end_time = (hour + minute + second) * 1000 + milisecond # 끝시간
    duration_time = int(float(t) * 1000) # 처리시간
    start_time = end_time - duration_time + 1 # 시작시간
    
    return [start_time, end_time]