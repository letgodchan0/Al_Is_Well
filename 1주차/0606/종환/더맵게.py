"""
return이 최소가 되는 조합
1순위. K보다 낮은 음식들을 섞어 최대한 K를 빨리 넘기는 것이 관건

만약, K가 지나치게 높아서 주어진 스코빌들을 모두 공식대로 합해도 K보다 낮은 음식 한개만 남는다면 -1
"""
import heapq
# heapq : push할 때마다 크기에 맞게 정렬된 상태로 입력된다.
#         다음 pop하기 전에 정렬할 필요가 없음

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    answer = 0

    # K보다 낮을 경우 계속
    while heap[0] < K:
        if len(heap) < 2:
            answer = -1
            break
        else:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
            answer += 1
            
    return answer