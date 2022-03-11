from itertools import combinations
import copy

n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
castle = [i for i in range(m)] # 성의 위치
ans = 0 # 제거할 수 있는 적의 최대 수

# 적의 위치 구하기
def get_enemy():
    enemy = []
    for i in range(n):
        for j in range(m):
            if copy_board[i][j]:
                enemy.append([i, j])
    return enemy

# 적을 공격하기
def attack(archer, enemy):
    global cnt
    remove = [] # 제거할 적 리스트

    for ay in archer:
        ax = n
        temp = [] # 제거할 수 있는 적 리스트

        for ex, ey in enemy:
            dist = abs(ax - ex) + abs(ay - ey) # 궁수와 적의 거리
            if dist <= d: # 거리가 d이하이면 리스트에 저장
                temp.append([dist, ex, ey])
        
        if temp: # 제거할 수 있는 적이 있다면
            temp.sort(key = lambda x: (x[0], x[2])) # 거리, y위치 순으로 정렬
            remove.append([temp[0][1], temp[0][2]]) # 가장 가깝고 왼쪽에 있는 적을 리스트에 저장

    # 적을 제거한다
    for x, y in remove:
        if copy_board[x][y]: # 아직 제거하지 않은 적인 경우 제거
            copy_board[x][y] = 0
            cnt += 1

    return cnt

for archer in combinations(castle, 3):
    copy_board = copy.deepcopy(board)
    cnt = 0 # 제거된 적의 수

    while True:
        enemy = get_enemy()
        if not enemy: break # 더 이상 제거할 적이 없다면 멈춘다

        attack(archer, enemy) # 적을 공격한다
        copy_board = [[0] * m] + copy_board[:n-1] # 적이 이동한다

    ans = max(ans, cnt)

print(ans)