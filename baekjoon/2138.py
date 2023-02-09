import copy

n = int(input())
bulb = list(map(int, input()))
result = list(map(int, input()))

case1 = copy.deepcopy(bulb) # 1번 스위치 누르지 않은 경우
case2 = copy.deepcopy(bulb) # 1번 스위치 누른 경우
case2[0], case2[1] = 1- case2[0], 1 - case2[1]

def flip(case):
    cnt = 0 # 스위치 누른 횟수

    for i in range(1, n):
        # i-1번 스위치 상태가 같은 경우 넘어간다
        if case[i-1] == result[i-1]:
            continue

        # 다르다면 스위치를 누른다
        for j in range(i-1, i+2):
            if j < n:
                case[j] = 1 - case[j]
        
        cnt += 1

    return cnt if case == result else 1e9

ans = min(flip(case1), flip(case2) + 1)
print(ans if ans != 1e9 else -1)