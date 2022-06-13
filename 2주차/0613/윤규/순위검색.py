# 정확성은 다 맞는데 효율성은 0 점 ㅡㅡ
def solution(info, query):
    answer = []
    # 24개의 리스트 만들고
    for i in ["c", "j", "p"]:
        for j in ['b', 'f']:
            for k in ['j', 's']:
                for l in ['c', 'p']:
                    globals()[f'{i+j+k+l}'] = []
    
    # info 나누기
    for i in range(len(info)):
        lan, job, car, food, score = map(str, info[i].split(' '))
        st = lan[0] + job[0] + car[0] + food[0]
        globals()[f'{st}'].append(score)

    # query로 받은거 갯수 구하기
    for i in range(len(query)):
        cnt = 0
        lan, job, car, food = map(str, query[i].split(' and '))
        food, score = map(str, food.split(' '))
        lan, job, car, food = lan[0], job[0], car[0], food[0]
        
        if lan == '-':
            
            lan = ["c", "j", "p"]
        if job == '-':
            job = ['b', 'f']
        if car == '-':
            car = ['j', 's']
        if food == '-':
            food = ['c', 'p']
        for p in lan:
            for j in job:
                for k in car:
                    for l in food:
                        st = p+j+k+l
                        for s in globals()[f'{st}']:
                            
                            if int(s) >= int(score):
                                cnt += 1
        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))