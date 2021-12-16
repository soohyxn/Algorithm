king, stone, n = input().split()
move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

king_x, king_y = ord(king[0]) - ord('A'), int(king[1]) - 1
stone_x, stone_y = ord(stone[0]) - ord('A'), int(stone[1]) - 1

for _ in range(int(n)):
    idx = move.index(input())
    kx, ky = king_x + dx[idx], king_y + dy[idx]

    if kx < 0 or kx > 7 or ky < 0 or ky > 7:
        continue
    if kx == stone_x and ky == stone_y:
        sx, sy = stone_x + dx[idx], stone_y + dy[idx]
        if sx < 0 or sx > 7 or sy < 0 or sy > 7:
            continue
        stone_x, stone_y = sx, sy
    king_x, king_y = kx, ky

print(f'{chr(king_x + ord("A"))}{king_y + 1}')
print(f'{chr(stone_x + ord("A"))}{stone_y + 1}')