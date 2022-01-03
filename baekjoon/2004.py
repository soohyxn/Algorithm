N, M = map(int, input().split())

def count_num(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

two_count = count_num(N, 2) - count_num(M, 2) - count_num(N-M, 2)
five_count = count_num(N, 5) - count_num(M, 5) - count_num(N-M, 5)
print(min(two_count, five_count))