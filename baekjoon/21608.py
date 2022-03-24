import sys
input = sys.stdin.readline

n = int(input())
likes = [[] for _ in range(n*n+1)] # 각 학생의 좋아하는 학생 번호 리스트
seat = [[0] * n for _ in range(n)] # 정해진 자리
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0] # 북서동남 ([조건 3] 행 -> 열 순으로 정하기 위해서)
ans = 0 # 만족도의 총 합

# 자리 정하기
for _ in range(n*n):
    temp = list(map(int, input().split()))
    likes[temp[0]] = temp[1:]

    ans_x, ans_y = 0, 0 # 최종 자리
    ans_like, ans_empty = -1, -1 # 좋아하는 학생 수의 최대값, 비어있는 자리 수의 최대값

    for x in range(n):
        for y in range(n):
            if seat[x][y] == 0: # 아직 자리가 비어있는 경우
                like, empty = 0, 0 # 좋아하는 학생 수, 비어있는 자리 수

                # 인접한 칸 확인
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seat[nx][ny] in temp: # 해당 인접칸에 좋아하는 학생이 있는 경우
                            like += 1
                        if seat[nx][ny] == 0: # 해당 인접칸이 비어있는 경우
                            empty += 1
                
                if like > ans_like or (like == ans_like and empty > ans_empty): # [조건 1] 좋아하는 학생 수가 더 많거나 [조건 2] 비어있는 칸이 더 많은 경우
                    ans_x, ans_y = x, y
                    ans_like, ans_empty = like, empty

    seat[ans_x][ans_y] = temp[0]

# 만족도의 총 합 구하기
for x in range(n):
    for y in range(n):
        cnt = 0 # 좋아하는 학생 수
        like = likes[seat[x][y]]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and seat[nx][ny] in like:
                cnt += 1
        
        if cnt > 0:
            ans += 10 ** (cnt - 1) # 만족도

print(ans)