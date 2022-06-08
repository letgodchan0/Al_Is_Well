def solution(progresses, speeds):
    answer = []
    while progresses: # progresses가 끝날 때까지
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))
