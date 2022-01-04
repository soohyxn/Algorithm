import math

N = int(input())
nums = [int(input()) for _ in range(N)]
diff = [abs(nums[i] - nums[i+1]) for i in range(N-1)] # 입력받은 숫자들의 차이
GCD = diff[0] # diff의 최대공약수
answer = []

# diff의 최대공약수 구하기
if len(diff) > 1:
    for i in range(1, len(diff)):
        GCD = math.gcd(GCD, diff[i])

# 구한 최대공약수의 약수 구하기
for i in range(2, int(GCD ** 0.5)+1):
    if GCD % i == 0:
        answer.append(i)
        if GCD // i != i:
            answer.append(GCD // i)

answer.append(GCD) # 마지막으로 최대공약수도 약수에 추가
answer.sort()
print(*answer)