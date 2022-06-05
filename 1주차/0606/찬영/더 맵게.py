import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        heapq.heapify(scoville)
        min1=heapq.heappop(scoville)
        min2=heapq.heappop(scoville)
        heapq.heappush(scoville, min1+2*min2)
        if len(scoville)==1 and scoville[0]<K:
            return -1
        answer+=1
    
    return answer