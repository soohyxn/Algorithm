def solution(dirs):
    move = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}
    x, y = 0, 0 # 시작 지점
    road = set()
    
    for dir in dirs:
        dx, dy = move[dir]
        nx, ny = x + dx, y + dy # 도착 지점
        
        # 이동 가능한 범위인 경우 해당 길 추가 (시작 지점 -> 도착지점, 도착 지점 -> 시작 지점을 같은 길로 취급한다)
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            road.add((x, y, nx, ny))
            road.add((nx, ny, x, y))
            x, y = nx, ny
            
    return len(road) // 2