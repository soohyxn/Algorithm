n = str(input())
left = n[:len(n)//2]
right = n[len(n)//2:]
l_sum = 0
r_sum = 0

for i in range(len(left)):
    l_sum += int(left[i])
    r_sum += int(right[i])

if l_sum == r_sum: print('LUCKY')
else: print('READY')