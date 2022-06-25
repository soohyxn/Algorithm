A, B = map(int, input().split())
N, M = map(int, input().split())
dir = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 동남서북
board = [[0] * B for _ in range(A)] # 각 위치별 로봇
robots = [] # 로봇정보 리스트
flag = False # 잘못된 명령인지 확인하는 플래그

for i in range(N):
    x, y, d = input().split() # 로봇의 위치, 방향
    x, y = int(x), int(y)
    robots.append([x-1, y-1, dir[d]])
    board[x-1][y-1] = i+1

for _ in range(M):
    idx, com, num = input().split() # 로봇번호, 명령, 명령 반복 횟수
    idx, num = int(idx), int(num)
    x, y, d = robots[idx-1] # 로봇의 위치, 방향

    # 왼쪽으로 회전하기
    if com == 'L':
        robots[idx-1][2] = (d + 3 * num) % 4
    # 오른쪽으로 회전하기
    elif com == 'R':
        robots[idx-1][2] = (d + num) % 4
    # 앞으로 한 칸 움직이기
    else:
        for _ in range(num):
            # 다음 위치
            nx = x + dx[d]
            ny = y + dy[d]

            # 로봇이 벽에 충돌하는 경우
            if nx < 0 or nx >= A or ny < 0 or ny >= B:
                flag = True
                print(f'Robot {idx} crashes into the wall')
                break

            # 로봇이 다른 로봇과 충돌하는 경우
            if board[nx][ny]:
                flag = True
                print(f'Robot {idx} crashes into robot {board[nx][ny]}')
                break

            board[x][y] = 0
            board[nx][ny] = idx
            robots[idx-1] = [nx, ny, d]
            x, y = nx, ny
    
    # 잘못된 명령인 경우
    if flag: break

# 정상 명령인 경우
if not flag: print('OK')