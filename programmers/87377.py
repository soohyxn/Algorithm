def solution(line):
    answer = []
    points = set()
    
    # 교점 구하기
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            
            # 두 직선이 평행 또는 일치하지 않는 경우, 교점을 구한다
            if (a * d) - (b * c) != 0:
                x = ((b * f) - (e * d)) / ((a * d) - (b * c))
                y = ((e * c) - (a * f)) / ((a * d) - (b * c))
            
            # 교점이 정수라면 집합에 추가
            if int(x) == x and int(y) == y:
                points.add((int(x), int(y)))
    
    # 별을 그릴 최소 사각형 범위 구하기
    start_x = min(p[0] for p in points)
    start_y = min(p[1] for p in points)
    end_x = max(p[0] for p in points)
    end_y = max(p[1] for p in points)
    
    # 별 그리기
    for y in range(end_y, start_y - 1, -1):
        result = ""
        for x in range(start_x, end_x + 1):
            if (x, y) in points:
                result += "*"
            else:
                result += "."
        answer.append(result)
    
    return answer