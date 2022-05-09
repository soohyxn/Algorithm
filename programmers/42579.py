from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(int) # 장르별 재생횟수
    plays_dict = defaultdict(list) # 장르별 노래 정보
    
    # 장르별 구분하기
    for i in range(len(genres)):
        genres_dict[genres[i]] += plays[i]
        plays_dict[genres[i]].append((plays[i], i))
    
    genres_sort = sorted(genres_dict.items(), key = lambda x: -x[1]) # 재생횟수 높은 순으로 장르 정렬
    
    # 앨범에 들어갈 노래 순서 구하기
    for genre, _ in genres_sort:
        plays_sort = sorted(plays_dict[genre], key = lambda x: (-x[0], x[1])) # 재생 횟수 높은 순 -> 고유번호 낮은 순으로 노래 정렬
        for i, play in enumerate(plays_sort):
            if i == 2: break # 노래 2개 수록
            answer.append(play[1])
        
    return answer