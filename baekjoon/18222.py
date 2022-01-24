k = int(input())

def recur(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return recur(n//2)
    else:
        return 1 - recur(n//2)

print(recur(k-1))