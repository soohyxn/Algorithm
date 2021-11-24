n = int(input())
tile = [0, 1, 2]
length = len(tile)

if n >= length:
	for i in range(length, n+1):
		tile.append((tile[i-1] + tile[i-2])% 15746)

print(tile[n])