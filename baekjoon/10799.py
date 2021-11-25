arr = input()
arr = arr.replace('()', 'L') # 레이저는 L로 바꿔줌
stack = []
count = 0

for i in range(len(arr)):
    if arr[i] == '(': # 막대기 시작일 경우 스택에 추가
        stack.append('(')
    elif arr[i] == 'L': # 레이저일 경우 스택 길이만큼 개수에 추가
        count += len(stack)
    else: # 막대기 끝일 경우 스택에서 막대기 제거 후 개수에 +1
        stack.pop()
        count += 1

print(count)