def solution(s):
    nums = list(map(int, s.split()))
    min_n, max_n = min(nums), max(nums)
    
    return str(min_n) + ' ' + str(max_n)