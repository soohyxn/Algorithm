def solution(k, tangerine):
    answer = 0
    tan_type = {} # 귤의 종류별 개수
    
    # 귤의 종류별 개수 구하기
    for t in tangerine:
        if t in tan_type:
            tan_type[t] += 1
        else:
            tan_type[t] = 1
    
    # 개수가 많은 순으로 정렬
    sort_tan_type = dict(sorted(tan_type.items(), key=lambda x: -x[1]))
    
    # 귤 종류의 최소값 구하기
    for t, count in sort_tan_type.items():
        if k <= 0:
            return answer
        k -= count
        answer += 1
    
    return answer