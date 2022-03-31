# 악보 바꾸기
def change(str):
    str = str.replace('C#', 'c')
    str = str.replace('D#', 'd')
    str = str.replace('F#', 'f')
    str = str.replace('G#', 'g')
    str = str.replace('A#', 'a')
    return str

def solution(m, musicinfos):
    answer = []
    m = change(m)
    
    for musicinfo in musicinfos:
        start, end, title, info = musicinfo.split(',')
        info = change(info)
        
        time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:])) # 재생 시간
        music = info * (time // len(info)) + info[:time % len(info)] # 전체 악보
        
        if m in music: # 조건에 일치하는 음악인 경우
            answer.append([title, time])
        
    if answer: 
        answer.sort(key = lambda x: -x[1]) # 재생 시간(내림차순) -> 입력 순서(오름차순)로 정렬 
        return answer[0][0]
    else:
        return '(None)'