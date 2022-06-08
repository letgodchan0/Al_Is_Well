import heapq

def solution(scovile, k):
    result = 0
    heapq.heapify(scovile)

    while scovile[0] < k:
        a = heapq.heappop(scovile) + (heapq.heappop(scovile) * 2)
        heapq.heappush(scovile, a)
        result += 1
        if len(scovile) == 1 and scovile[0] < k:
            return -1
    return result