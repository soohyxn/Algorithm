def solution(lottos, win_nums):
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    
    lotto, win = set(lottos), set(win_nums)
    ints = len(lotto & win)
    zero = lottos.count(0)
    
    max_rank, min_rank = rank[ints + zero], rank[ints]
    return [max_rank, min_rank]