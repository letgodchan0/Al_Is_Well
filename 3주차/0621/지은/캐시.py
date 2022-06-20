def solution(cacheSize, cities):
    if cacheSize==0:
        return len(cities) * 5  #크기가 0인 경우 계속 cache miss이므로

    time = 0    #실행시간
    cache = [0] * cacheSize     #도시 이름
    c_idx = [0] * cacheSize     #언제 저장되었는지
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        #LRU: 가장 오랫동안 참조되지 않은 페이지를 교체
        if cities[i] in cache:
            idx = cache.index(cities[i])
            c_idx[idx] = i
            time += 1
        else:
            if 0 in cache:  #캐시에 다 저장되어있지 않았을 경우
                idx = cache.index(0)
            else:
                idx = c_idx.index(min(c_idx))
            cache[idx] = cities[i]
            c_idx[idx] = i
            time += 5

    return time

