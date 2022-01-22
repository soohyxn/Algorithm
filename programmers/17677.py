from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    
    # 두 문자열의 다중 집합 구하기
    set_str1 = Counter([str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()])
    set_str2 = Counter([str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()])

    # 다중 집합의 교집합과 합집합 구하기
    intersec = list((set_str1 & set_str2).elements())
    union = list((set_str1 | set_str2).elements())

    if not union:
        return 65536
    else:
        return int(len(intersec) / len(union) * 65536)