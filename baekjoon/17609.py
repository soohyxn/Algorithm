T = int(input())

for _ in range(T):
    s = input()
    l = len(s)

    # 회문인 경우
    if s == s[::-1]:
        print(0)
        continue

    for i in range(l//2):
        if s[i] != s[l-i-1]:
            s1 = s[:i] + s[i+1:] # 왼쪽 문자 삭제
            s2 = s[:l-i-1] + s[l-i:] # 오른쪽 문자 삭제

            # 유사 회문인 경우
            if s1 == s1[::-1] or s2 == s2[::-1]:
                print(1)
            # 일반 문자열인 경우
            else:
                print(2)
            break