from itertools import permutations

n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
ans = 0 # 최대 득점

def game(players):
    hitter, score = 0, 0 # 타자 번호, 득점

    for inning in innings:
        out, b1, b2, b3 = 0, 0, 0, 0 # 아웃 수, 각 base의 주자 수

        while out < 3:
            player = players[hitter] # 현재 타자

            if inning[player] == 0: # 아웃 - 모두 진루하지 못하고 아웃 하나 증가
                out += 1
            elif inning[player] == 1: # 안타 - 모두 한 루씩 진루
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[player] == 2: # 2루타 - 모두 두 루씩 진루
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif inning[player] == 3: # 3루타 - 모두 세 루씩 진루
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif inning[player] == 4: # 홈런 - 모두 홈까지 진루
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0

            hitter = (hitter + 1) % 9 # 다음 타자로
    
    return score

for per in permutations(range(1, 9), 8):
    players = list(per[:3]) + [0] + list(per[3:])
    result = game(players)
    ans = max(ans, result) # 득점 갱신

print(ans)