"""
progresses 리스트 내에 있는 기능이 남아있는 동안 계속되는 while 루프
며칠째에 배포되는지는 상관 없으므로, 리스트 첫번째 원소가 100 이상이 아니라면,
  리스트 모든 요소에 각각 speeds만큼을 더함
  만약 첫번째 원소가 100 이상이 된다면, tmp = 0으로 초기화하고 이하 while로 반복
    첫번째 원소가 100 이상이라면...
      첫번째 원소를 제거(popleft)
      tmp += 1
    result.append(tmp)

"""
from collections import deque

def solution(progresses, speeds):
    q = deque(progresses)
    speeds_q = deque(speeds)
    answer = []

    while q:
        if q[0] < 100:
            for i in range(len(q)):
                q[i] += speeds_q[i]
        elif q[0] >= 100:
            tmp = 0
            while q[0] >= 100:
                q.popleft()
                speeds_q.popleft()
                tmp += 1
            answer.append(tmp)
    
    return answer

print(solution([93, 30, 55], [1, 30, 5]))

# deque index out of range