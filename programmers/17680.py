def solution(cacheSize, cities):
    cache = []
    answer = 0
    
    for city in cities:
        if city.lower() in cache: # cache hit
            answer += 1
            cache.remove(city.lower()) # 캐시의 가장 뒤로 보내기 위해 삭제
        else: # cache miss
            answer += 5
            if cacheSize == 0: # 캐시 사이즈가 0이라면 바로 넘어간다
                continue
            if len(cache) >= cacheSize: # 캐시 사이즈보다 크거나 같다면 가장 오래된 캐시 삭제
                cache.pop(0)
        cache.append(city.lower()) # 캐시에 저장