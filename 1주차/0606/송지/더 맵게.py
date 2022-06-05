import heapq

def solution(scov, K):
    ans = 0
    
    heapq.heapify(scov)
    
    while scov[0] < K:
        try:
            a = heapq.heappop(scov)
            b = heapq.heappop(scov)
            heapq.heappush(scov, a + b * 2)
            ans += 1
        except:
            return -1
        
    return ans