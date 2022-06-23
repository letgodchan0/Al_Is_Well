from collections import deque

def solution(cacheSize, cities):
    answer = 0
    buffer = deque()

    if cacheSize == 0:
        return len(cities) * 5
    else:
        for i in cities:
            i = i.lower()
            if i in buffer:
                answer += 1
            else:
                answer += 5
            
            if i in buffer:
                buffer.remove(i)
            else:
                if len(buffer) >= cacheSize:
                    buffer.popleft()
            buffer.append(i)
    return answer
