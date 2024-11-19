def solution(sequence):
    # 연속 펄스 수열 구하기
    list1, list2 = [], []
    for i, s in enumerate(sequence):
        if i % 2 == 0:
            # case1: 1, -1, 1, -1
            list1.append(s * 1)
            # case2: -1, 1, -1, 1
            list2.append(s * -1)
        else:
            # case1: 1, -1, 1, -1
            list1.append(s * -1)
            # case2: -1, 1, -1, 1
            list2.append(s * 1)
    
    # 부분 수열의 최대값 구하기
    dp1, dp2 = [list1[0]], [list2[0]]
    for i in range(1, len(list1)):
        dp1.append(max(dp1[i-1] + list1[i], list1[i]))
        dp2.append(max(dp2[i-1] + list2[i], list2[i]))
    
    return max(max(dp1), max(dp2))