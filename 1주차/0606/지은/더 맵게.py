import heapq    #데이터를 정렬된 상태로 저장할 수 있다. 최소힙
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville)==1:
            return -1
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + (b * 2))
            answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))