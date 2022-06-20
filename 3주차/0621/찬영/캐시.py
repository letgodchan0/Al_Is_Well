def solution(cacheSize, cities):
    cache = []
    cnt = 0
    cities = [i.upper() for i in cities]
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        # Cache  Miss
        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
            cnt += 5
        # Cache Hit
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            cnt += 1
    return cnt