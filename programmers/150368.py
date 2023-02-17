from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    dc_percent = [10, 20, 30, 40] # 이모티콘 할인율
    
    # 모든 할인율 경우의 수 완전탐색
    for discounts in product(dc_percent, repeat = len(emoticons)):
        result = [0, 0] # 이모티콘 플러스 가입 수, 이모티콘 매출액
        
        for user_discount, user_money in users:
            money = 0 # 구매비용
            
            # 해당 사용자의 이모티콘 구매비용을 구한다
            for emoticon, discount in zip(emoticons, discounts):
                # 할인율이 해당 사용자의 할인율 기준 이상이라면 이모티콘을 구매한다
                if discount >= user_discount:
                    money += emoticon * (1 - discount / 100)
            
            # 구매비용이 해당 사용자의 구매비용 기준 이상이라면 이모티콘 플러스에 가입한다
            if money >= user_money:
                result[0] += 1
            else:
                result[1] += money
                
        answer = max(answer, result)

    return answer