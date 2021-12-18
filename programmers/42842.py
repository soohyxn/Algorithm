def solution(brown, yellow):
    answer = []
    
    for height in range(3, brown):
        width = (brown + yellow) / height
        if width < height:
            continue
        if yellow == (width - 2) * (height -2):
            answer = [width, height]
            
    return answer