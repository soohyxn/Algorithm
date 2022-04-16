def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2], '*': [3, 0], 0: [3, 1], '#': [3, 2]} # 각 번호의 키패드 위치
    left, right = keypad['*'], keypad['#'] # 왼손, 오른손 위치
    
    for num in numbers:
        if num in [1, 4, 7]: # 왼쪽 열인 경우
            answer += 'L'
            left = keypad[num]
        elif num in [3, 6, 9]: # 오른쪽 열인 경우
            answer += 'R'
            right = keypad[num]
        else: # 가운데 열인 경우
            loc = keypad[num]
            left_dist = abs(left[0] - loc[0]) + abs(left[1] - loc[1]) # 왼손과의 거리
            right_dist = abs(right[0] - loc[0]) + abs(right[1] - loc[1]) # 오른손과의 거리
            
            if left_dist > right_dist:
                answer += 'R'
                right = keypad[num]
            elif left_dist < right_dist:
                answer += 'L'
                left = keypad[num]
            else: # 거리가 같은 경우
                if hand == 'left':
                    answer += 'L'
                    left = keypad[num]
                else:
                    answer += 'R'
                    right = keypad[num]
                    
    return answer