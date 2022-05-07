from collections import defaultdict

T = int(input())

for _ in range(T):
    w = input()
    k = int(input())
    ans_min, ans_max = len(w), -1 # 어떤 문자를 K개를 포함하는 가장 짧은 연속 문자열의 길이, 가장 긴 연속 문자열의 길이
    alpha = defaultdict(list)

    # 알파벳별 위치 저장
    for idx, val in enumerate(w):
        alpha[val].append(idx)

    # 슬라이딩 윈도우
    for val in alpha.values():
        for i in range(len(val)-k+1):
            ans_min = min(ans_min, val[i+k-1] - val[i] + 1)
            ans_max = max(ans_max, val[i+k-1] - val[i] + 1)

    print(f'{ans_min} {ans_max}' if ans_max != -1 else -1)