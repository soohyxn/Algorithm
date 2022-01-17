def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_list = list(skill)
        for sk in skill_tree:
            if sk in skill and sk != skill_list.pop(0): # 스킬 순서와 다르면 break
                break
        else:
            answer += 1
        
                
    return answer