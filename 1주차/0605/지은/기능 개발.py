def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0

        for i in range(len(progresses)):    
            progresses[i] += speeds[i]

        for progress in progresses: #진행도가 100이상인 기능 찾기
            if progress >=100:
                cnt += 1
            else:                   #앞의 기능과 같이 배포해야되므로
                break

        if cnt > 0:
            answer.append(cnt)

        for _ in range(cnt):        #배포한 기능 삭제
            del progresses[0]
            del speeds[0]

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
