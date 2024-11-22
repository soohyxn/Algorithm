N, X = map(int, input().split())
burger = [1] * 51 # 버거의 레이어 개수
patty = [1] * 51 # 버거의 패티 개수

# 버거의 레이어와 패티 개수 구하기
for i in range(1, N+1):
    burger[i] = 1 + burger[i-1] + 1 + burger[i-1] + 1
    patty[i] = patty[i-1] + 1 + patty[i-1]

def eat(n, x):
    # 레벨이 0이면 무조건 패티이므로 바로 리턴
    if n == 0:
        return x
    
    # 레벨이 1이상 이면서 1장을 먹으면 무조건 번이므로 0 리턴
    if x == 1:
        return 0
    # case1) 가운데 패티 전까지 먹은 경우
    elif x <= 1 + burger[n-1]:
        return eat(n-1, x-1) # 맨 아래 번을 뺀다
    # case2) 딱 가운데 패티까지 먹은 경우
    elif x == 1 + burger[n-1] + 1:
        return patty[n-1] + 1
    # case3) 마지막 번 전까지 먹은 경우
    elif x <= burger[n-1] + 1 + burger[n-1] + 1:
        return patty[n-1] + 1 + eat(n-1, x-burger[n-1]-2)
    # case4) 다 먹은 경우
    else:
        return patty[n]

print(eat(N, X))