from collections import defaultdict

def solution(id_list, report, k):
    report_list = defaultdict(set) # 유저별 신고한 유저
    reported_list = defaultdict(set) # 유저별 신고 당한 유저
    answer = []
    
    for r in report:
        a, b = r.split(" ")
        report_list[a].add(b)
        reported_list[b].add(a)

    for id in id_list:
        cnt = 0 # 메일을 받은 횟수
        for user in report_list[id]:
            if len(reported_list[user]) >= k: # k번 이상 신고 당한 경우
                cnt += 1
        answer.append(cnt)
        
    return answer