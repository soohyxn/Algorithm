def solution(n, s, a, b, fares):
    graph = [[1e9] * n for _ in range(n)] # 최저요금 리스트
    answer = 1e9
    
    # 요금 저장
    for x, y, c in fares:
        graph[x-1][x-1] = 0
        graph[y-1][y-1] = 0
        graph[x-1][y-1] = c
        graph[y-1][x-1] = c
    
    # 모든 지점에서 모든 지점까지 최저요금 구하기 - 플로이드 워셜
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                    
    # 모든 경유지 기준으로 최저요금 구하기
    for i in range(n):
        answer = min(answer, graph[s-1][i] + graph[i][a-1] + graph[i][b-1])
    
    return answer