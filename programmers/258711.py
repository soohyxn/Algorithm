def solution(edges):
    answer = [0, 0, 0, 0] # 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수
    graph = {} # 정점별 간선의 수를 담은 딕셔너리
    
    # 정점별 간선의 수 구하기
    for a, b in edges:
        if a not in graph:
            graph[a] = [0, 0]
        
        if b not in graph:
            graph[b] = [0, 0]
        
        graph[a][0] += 1 # 나가는 간선의 수
        graph[b][1] += 1 # 들어오는 간선의 수
    
    # 생성한 정점과 그래프의 수 구하기
    for v, count in graph.items():
        # 1. 생성한 정점 : 나가는 간선의 수 2개, 들어오는 간선의 수 0개
        if count[0] >= 2 and count[1] == 0:
            answer[0] = v
        # 2. 막대 모양 그래프 : 나가는 간선의 수 0개, 들어오는 간선의 수 1개 이상
        elif count[0] == 0 and count[1] >= 1:
        # 3. 8자 모양 그래프 : 나가는 간선의 수 2개 이상, 들어오는 간선의 수 2개 이상
            answer[2] += 1
        elif count[0] >= 2 and count[1] >= 2:
            answer[3] += 1
    
    # 4. 도넛 모양 그래프 : 생성한 정점에서 나가는 간선의 수 - 막대 모양 그래프의 수 - 8자 모양 그래프의 수
    answer[1] = graph[answer[0]][0] - answer[2] - answer[3]
        
    return answer