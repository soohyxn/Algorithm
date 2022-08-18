N, k = map(int, input().split())
digit = 1 # 자릿수
num = 9 # 해당 자릿수의 숫자 개수
ans = 0 # 현재수

# 자릿수에 맞게 빼준다
while k > digit * num:
    k -= digit * num # 1의 자리는 1*9개, 10자리는 2*90개
    ans += num # 현재수 갱신

    # 자릿수 이동
    digit += 1
    num *= 10

ans = (ans + 1) + (k - 1) // digit # 남은수를 현재수에 더한다
print(str(ans)[(k-1) % digit] if ans <= N else -1)