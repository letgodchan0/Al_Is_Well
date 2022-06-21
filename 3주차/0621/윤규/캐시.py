def solution(cacheSize, cities):
    answer = 0
    cache = [''] * cacheSize
    if cacheSize == 0:
        return len(cities) * 5
    for citi in cities:
        citi = citi.lower()
        if citi in cache:
            cache.append(cache.pop(cache.index(citi)))
            answer += 1
        else:
            cache.pop(0)
            cache.append(citi)
            answer += 5
    
    return answer


cacheSize = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize, cities))