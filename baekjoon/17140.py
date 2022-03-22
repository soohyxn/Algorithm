from cProfile import label
from collections import Counter

r, c, k = map(int, input().split())
r, c = r-1, c-1
a = [list(map(int, input().split())) for _ in range(3)]
time = 0 # 최소 시간

def R():
    max_len = 0 # 최대 길이

    # 배열에 연산 적용하기
    for i in range(len(a)):
        arr = [x for x in a[i] if x != 0] # 정렬 대상에 0은 제외
        arr = list(map(list, Counter(arr).items()))
        arr.sort(key = lambda x: (x[1], x[0])) # 등장 횟수 -> 숫자 순으로 정렬
        a[i] = list(sum(arr, []))[:100] # 크기 100까지만 저장
        max_len = max(max_len, len(a[i]))

    # 길이 맞추기
    for i in range(len(a)):
        if len(a[i]) < max_len:
            a[i] += [0] * (max_len - len(a[i]))

while True:
    # 100초가 지나는 경우
    if time > 100:
        print(-1)
        break

    # a[r][c] = k가 되기 위한 최소 시간 출력
    row, col = len(a), len(a[0])
    if r < row and c < col and a[r][c] == k:
        print(time)
        break

    if row >= col: # R 연산
        R()
    else: # C 연산
        a = list(zip(*a)) # transpose(행과 열 바꾸기)
        R()
        a = list(zip(*a))

    time += 1