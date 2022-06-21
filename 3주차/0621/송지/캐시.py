def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize:
        for city in cities:
            c = city.upper()
            if c not in cache:
                answer += 5
                if len(cache) < cacheSize:
                    cache.append(c)
                else:
                    cache.pop(0)
                    cache.append(c)
            else:
                answer += 1
                cache.remove(c)
                cache.append(c)
    else:
        answer += len(cities) * 5
                
    return answer