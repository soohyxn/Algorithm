n = int(input())
numbers = list(map(int, input().split()))
answer = 0

for num in numbers:
	count = 0
	if num > 1 :
		for i in range(2, num):
			if num % i == 0:
				count += 1

		if count == 0:
			answer += 1
				
print(answer)